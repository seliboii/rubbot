import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge
from std_msgs.msg import Float64
import numpy as np
import cv2
import torch
from sensor_msgs.msg import PointCloud2, PointField
import struct
import ctypes
from tf2_ros import TransformBroadcaster
from tf2_ros.transform_listener import TransformListener
from geometry_msgs.msg import Pose, PoseStamped, Point
from geometry_msgs.msg import TransformStamped
from tf2_ros.buffer import Buffer
import tf2_geometry_msgs
import os
import time

from detector4 import Detector

class Ros2Detector(Node):
    def __init__(self):
        super().__init__('ros2_detector')
        self.detector = Detector()  # Assuming 10 categories for example
        self.load_model()
        self.bridge = CvBridge()
        self.publisher_realsense = self.create_publisher(Image, 'dl_realsense', 10)
        self.publisher_gripcam = self.create_publisher(Image, 'dl_gripcam', 10)
        self.publisher_gripper_angle = self.create_publisher(Float64,'gripper_angle',10)
        self.publisher_gripper_position = self.create_publisher(Point,'gripper_position',10)
        self.subscription = self.create_subscription(Image,'/image_rect',self.image_callback,10)
        self.subscription2 = self.create_subscription(Image,'/camera/color/image_raw',self.image_callback2,10)
        self.subscription_depth_info = self.create_subscription(CameraInfo,'/camera/depth/camera_info', self.depth_info_callback, 10)
        self.subscription_depth = self.create_subscription(Image, '/camera/aligned_depth_to_color/image_raw', self.depth_callback, 10)
        self.subscription_gripper_info = self.create_subscription(Image, '/camera1/camera_info', self.gripper_info_callback, 10)
        self.subscription
        self.subscription2
        self.subscription_depth
        self.subscription_depth_info
        self.gripcam_resolution = (640, 480)  # Resolution of image_rect topic
        self.realsense_resolution = (1280, 720)  # Resolution of camera/color/image_raw topic
        self.depth_info = None
        self.depth_image = None
        self.depth_received = False
        self.publisher_pose = self.create_publisher(PoseStamped, '/move_base_simple/goal', 10)  
        self.tf_broadcaster = TransformBroadcaster(self)
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer,self)
        self.tf_frame_ids = {}
        self.last_save_time = time.time()

    def depth_info_callback(self, msg):
        self.depth_info = msg

    def gripper_info_callback(self, msg):
        self.gripper_info = msg

    def depth_callback(self, msg):
        self.depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        self.depth_received = True

    def load_model(self):
        #model_path = "final_model4.pt"
        #model_path = "v1.pt"
        model_path = "modelV3.pt"
        state_dict = torch.load(model_path, map_location=torch.device('cpu'))
        self.detector.load_state_dict(state_dict)

    def resize_bounding_boxes(self, bbs, src_resolution, target_resolution):
        ratio_x = target_resolution[0] / src_resolution[0]
        ratio_y = target_resolution[1] / src_resolution[1]
        resized_bbs = []
        for bb in bbs:
            resized_bb = {
                'x': int(bb['x'] * ratio_x),
                'y': int(bb['y'] * ratio_y),
                'width': int(bb['width'] * ratio_x),
                'height': int(bb['height'] * ratio_y),
                'label': bb['label']  # Include category in resized bounding boxes
            }
            resized_bbs.append(resized_bb)
        return resized_bbs
    
    def get_depth_at_point(self, x, y):
        if self.depth_image is None:
            return None
        x_int = int(round(x))
        y_int = int(round(y))
        depth = self.depth_image[y_int, x_int]
        return depth
    
    def get_pointcloud_at_point(self, x, y):
        if self.depth_image is None or self.depth_info is None:
            return None
        fx = self.depth_info.k[0]  # Focal length in x direction
        fy = self.depth_info.k[4]  # Focal length in y direction
        cx = self.depth_info.k[2]  # Principal point in x direction
        cy = self.depth_info.k[5]  # Principal point in y direction
        
        # Convert center_x and center_y to integers
        center_x = int(round(x))
        center_y = int(round(y))
        
        depth = self.depth_image[center_y, center_x]
        if depth == 0:
            return None
        z = float(depth)  # Convert depth to float
        x = (center_x - cx) * depth / fx
        y = (center_y - cy) * depth / fy
        return x, y, z
    
    def save_image_with_bb(self, cv_image, bbs, image_id, folder_path):
        for i, bb in enumerate(bbs):
            x, y, width, height = bb['x'], bb['y'], bb['width'], bb['height']
            label = bb.get("label") or "unknown"
            class_instance_name = f"{label}_{image_id}_{i}"
            image_path = os.path.join(folder_path, f"{class_instance_name}.png")

            # Draw rectangle around the bounding box
            cv2.rectangle(cv_image, (x, y), (x + width, y + height), (0, 255, 0), 2)
            # Draw label
            cv2.putText(cv_image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Save the image with bounding box
            cv2.imwrite(image_path, cv_image)

    
    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        tensor_frame = torch.tensor(cv_image, dtype=torch.float32).permute(2, 0, 1) / 255.0
        tensor_frame = tensor_frame.unsqueeze(0)
        output = self.detector(tensor_frame)
        bbs = self.detector.out_to_bbs(output)

        if bbs and bbs[0]:
            highest_score_bb = max(bbs[0], key=lambda x: x['score'])  # Get the bounding box with the highest score
            x, y, width, height = highest_score_bb['x'], highest_score_bb['y'], highest_score_bb['width'], highest_score_bb['height']
            x, y, width, height = int(x), int(y), int(width), int(height)  # Convert to integers
            x2, y2 = x + width, y + height

            # Calculate center of the bounding box
            bb_center_x = (x + x2) // 2
            bb_center_y = (y + y2) // 2
                    
            # Extract the region of interest (ROI) defined by the bounding box
            roi = cv_image[y:y2, x:x2]
                    
            # Calculate edges using Canny edge detection
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray_roi, 100, 150)  # Adjust the threshold values (low, high) here
                    
            # Calculate moments for the ROI
            moments = cv2.moments(edges)
            mu20 = moments['mu20']
            mu11 = moments['mu11']
            mu02 = moments['mu02']
            theta = 0.5 * np.arctan2(2 * mu11, (mu20 - mu02 + np.sqrt(4 * mu11**2 + (mu20 - mu02)**2)))
                    
            # Convert theta to degrees
            theta_degrees = np.degrees(theta)

            turning_angle = theta_degrees  #Check this with Lee.

            if turning_angle > 10:
                # Create a Float64 ROS message and set its data field
                angle_msg = Float64()
                angle_msg.data = 90 -(turning_angle)
                        
                # Publish the Float64 message
                self.publisher_gripper_angle.publish(angle_msg)

            # Calculate center of the image
            img_center_x = cv_image.shape[1] // 2
            img_center_y = cv_image.shape[0] // 2
                
            # Calculate displacement of bounding box center from image center
            displacement_x = bb_center_x - img_center_x
            displacement_y = bb_center_y - img_center_y

            # Now into cm
            displacement_x = (displacement_x * 22) / 640
            displacement_y = -(displacement_y * 17.5) / 480

            center_position = Point()
            center_position.x = displacement_x/100
            center_position.y = displacement_y/100
            center_position.z = 16.5/100

            self.publisher_gripper_position.publish(center_position)

            # Draw text displaying the displacement from the center on the original image
            displacement_text = f"Displacement: ({displacement_x}, {displacement_y})"
            cv2.putText(cv_image, displacement_text, (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 2)

            # Draw text displaying the second moment on the original image
            text_second_moment = f"Second Moment: {theta_degrees:.2f} degrees"
            #cv2.putText(cv_image, text_second_moment, (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Draw text displaying the detected label on the original image
            label = highest_score_bb.get("label") 
            text_label = f"Detected: {label}"
            cv2.putText(cv_image, text_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Draw rectangle around the bounding box on the original image
            cv2.rectangle(cv_image, (x, y), (x2, y2), (0, 255, 0), 2)
                    
            # Convert edges to color and overlay on the original image
            edges_color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            cv_image[y:y2, x:x2] = cv2.addWeighted(roi, 0.4, edges_color, 0.6, 0)

        # Convert the final image to a ROS message
        msg_with_edges = self.bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
            
        # Publish the image message
        self.publisher_gripcam.publish(msg_with_edges)


    def image_callback2(self, msg):
        current_time = time.time()
        elapsed_time = current_time - self.last_save_time
        
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        tensor_frame = torch.tensor(cv_image, dtype=torch.float32).permute(2, 0, 1) / 255.0
        tensor_frame = tensor_frame.unsqueeze(0)
        output = self.detector(tensor_frame)
        bbs = self.detector.out_to_bbs(output)
        resized_bbs = self.resize_bounding_boxes(bbs[0], self.realsense_resolution, self.realsense_resolution)

        poses = []  # List to store poses of all detected objects
        bb_list = []  # List to store bounding boxes of all detected objects

        label_counts = {}

        for bb in resized_bbs:
            i=0
            x, y, width, height = bb['x'], bb['y'], bb['width'], bb['height']
            center_x = x + width / 2 
            center_y = y + height / 2 

            pointcloud_point = self.get_pointcloud_at_point(center_x, center_y)
            if pointcloud_point is None:
                continue
            final_x, final_y, depth = pointcloud_point

            pose_msg = PoseStamped()
            pose_msg.header.stamp = self.get_clock().now().to_msg() 
            pose_msg.header.frame_id = 'camera_link'
            pose_msg.pose.position.y = -final_x / 1000
            pose_msg.pose.position.z = -final_y / 1000
            pose_msg.pose.position.x = depth / 1000
            poses.append(pose_msg)  # Store the pose in the list

            label = bb.get("label") 

            if label in label_counts:
                # Increment the count for this label
                label_counts[label] += 1
                # Append numerical suffix to the label
                labeled_label = f"{label}{label_counts[label]}"
            else:
                # If label doesn't exist, initialize count to 1
                label_counts[label] = 1
                labeled_label = label

            # Generate a unique TF frame ID for each object based on its label
            tf_frame_id = f'/{labeled_label}'
            # Store the TF frame ID in the dictionary
            self.tf_frame_ids[label] = tf_frame_id

            # Create a TransformStamped message
            transform = TransformStamped()
            transform.header.stamp = self.get_clock().now().to_msg()
            transform.header.frame_id = 'camera_link'  # Change to your camera frame ID
            transform.child_frame_id = tf_frame_id
            transform.transform.translation.x = depth / 1000
            transform.transform.translation.y = -final_x / 1000
            transform.transform.translation.z = -final_y / 1000
            transform.transform.rotation.w = 1.0  # No rotation for simplicity
            
            # Broadcast the TF transform
            self.tf_broadcaster.sendTransform(transform)

            print("Detected label:", label)
            print("Center coordinates (x, y, z):", final_x, final_y, depth)

            bb_list.append(bb)  # Store the bounding box in the list

            cv2.rectangle(cv_image, (x, y), (x + width, y + height), (0, 255, 0), 2)
            cv2.putText(cv_image, f"{labeled_label}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            if elapsed_time >= 5:
                image_id = msg.header.stamp.sec
                self.save_image_with_bb(cv_image.copy(), resized_bbs, image_id, "Pictures")
                self.last_save_time = current_time

        msg_with_bounding_box = self.bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
        self.publisher_realsense.publish(msg_with_bounding_box)

        # Publish all detected objects together
        for pose in poses:
            self.publisher_pose.publish(pose)

def main(args=None):
    rclpy.init(args=args)
    ros2_detector = Ros2Detector()
    rclpy.spin(ros2_detector)
    ros2_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()