#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py.point_cloud2 import create_cloud_xyz32
import numpy as np
import ctypes
import struct
import math
import sensor_msgs_py.point_cloud2 as pc2
import copy
from sensor_msgs.msg import PointField
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped, Pose, PointStamped
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
import tf2_geometry_msgs
from tf2_ros import TransformException

# To not block transform listener?? idk
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup, ReentrantCallbackGroup




# multithreaded executor
# reen

class Detection(Node):

    def __init__(self):
        super().__init__('detection')

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        

        # Subscribe to the original pointcloud
        self.create_subscription(PointCloud2, '/camera/depth/color/points_throttle', self.cloud_callback, 2, callback_group=ReentrantCallbackGroup)

        # Initialize the publisher of our filtered pointcloud
        self._pub = self.create_publisher(PointCloud2, '/camera/depth/color/ds_points', 10)

        self._object_pub = self.create_publisher(PointStamped,'/object/position',10)       


        # Initialize the transform broadcaster
        # self._tf_broadcaster = TransformBroadcaster(self)

    def compute_transform(self, msg: PointCloud2, point):
        

        self.get_logger().info('cock')
        try:
            t = self.tf_buffer.lookup_transform(
                'map', 
                msg.header.frame_id, 
                msg.header.stamp,   #TODO fix timestamping
                timeout=rclpy.duration.Duration(seconds=8.2)
                )
        except TransformException as ex:
            self.get_logger().info(f'Transform failed: {ex}')
            return
        

        msg = PointStamped()
        msg.point.x = float(point[0])
        msg.point.y = float(point[1])
        msg.point.z = float(point[2])
        msg.header.frame_id = 'camera_depth_optical_frame'
        msg.header.stamp = msg.header.stamp

        ass = tf2_geometry_msgs.do_transform_point(msg, t)

        self._object_pub.publish(ass)


    def cloud_callback(self, msg: PointCloud2):

        # Convert ROS -> NumPy
        gen = pc2.read_points_numpy(msg, skip_nans=True)
        xyz = gen[:,:3]
        rgb = np.empty(xyz.shape, dtype=np.uint32)

        for idx, x in enumerate(gen):
            c = x[3]
            s = struct.pack('>f' , c)
            i = struct.unpack('>l', s)[0]
            pack = ctypes.c_uint32(i).value
            rgb[idx, 0] = np.asarray((pack >> 16) & 255, dtype=np.uint8) 
            rgb[idx, 1] = np.asarray((pack >> 8) & 255, dtype=np.uint8) 
            rgb[idx, 2] = np.asarray(pack & 255, dtype=np.uint8)

        rgb = rgb.astype(np.float32) / 255

        # We have to segmentate the cloud by color and distance
        ds_pointcloud = self.filter_points(xyz, rgb, msg)

        #self.get_logger().info(f'{ds_pointcloud}')
        self._pub.publish(ds_pointcloud)


    def filter_points(self, points, colors, pointcloud):

        # Tip: you can filter all points which are further away than 0.9m or are below ground
        distance_threshold = 1.4

        # Here we "segmentate" the pointcloud, only return those points in the pointcloud that match our criteria
        valid_points = [
            (point[0], point[1], point[2], color[0], color[1], color[2]) 
            for point, color in zip(points, colors)
            if point[2] < distance_threshold and (self.detect_red(color,point, pointcloud))   
             ]
        
        
        #if not valid_points:
            #self.get_logger().info('No object detected!')

        # Afer a lot of attempts, lets just manually create a PointCloud2 objects

        # We manually create the fields of the pointcloud x,y,z,rgb
        fields = [
            PointField(name="x", offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name="y", offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name="z", offset=8, datatype=PointField.FLOAT32, count=1),
            PointField(name="rgb", offset=12, datatype=PointField.UINT32, count=1),
        ]

        # Same values as the original pointcloud
        header = pointcloud.header
        height = 1 
        width = len(valid_points)

        # Create a NumPy array to hold the data
        place_holder = np.zeros((width, len(fields)), dtype=np.float32)

        # We extract the coordinates of our valid points in the pointcloud to give to the data
        for i, point in enumerate(valid_points):
            place_holder[i, 0] = point[0]  # x
            place_holder[i, 1] = point[1]  # y
            place_holder[i, 2] = point[2]  # z

            if i == 0:
                self.compute_transform(pointcloud, point)


            # Here we unpack the RGB values of the points from uint32 to a range from 0-1
            rgb_value = (int(point[3] * 120) << 16) + (int(point[4] * 120) << 8) + int(point[5] * 120)
            place_holder[i, 3] = rgb_value / 16777215.0

        # Convert the NumPy array to bytes
        data = place_holder.tobytes()

        # # This was literally trial and error, checking the rviz2 to see if the sizes matched
        point_step = len(fields) * 4  

        # We now create the new segmentated PointCloud2 message, same structure as the original
        filtered_pointcloud = PointCloud2(
            header=header,
            height=height,
            width=width,
            fields=fields,
            is_bigendian=False,
            point_step=point_step,
            row_step=width * point_step,
            is_dense=True,
            data=data
        )

        return filtered_pointcloud

    # For detecting the ball
    def detect_red(self, color, point, pointcloud):
        if color[0] > 0.6 and color[1] < 0.3 and color[2] < 0.3:  #if color[0] > 0.5 and color[1] < 0.4 and color[2] < 0.4:
            
            # try:
            #     t = self.tf_buffer.lookup_transform(
            #         'map', 
            #         pointcloud.header.frame_id, 
            #         rclpy.time.Time(),
            #         timeout=rclpy.duration.Duration(seconds=0.05)
            #         )
            # except:
            #     self.get_logger().info(str(pointcloud.header.stamp))
            #     return
            

            # msg = PointStamped()
            # msg.point.x = float(point[0])
            # msg.point.y = float(point[1])
            # msg.point.z = float(point[2])
            # msg.header.frame_id = 'camera_depth_optical_frame'
            # msg.header.stamp = pointcloud.header.stamp

            # ass = tf2_geometry_msgs.do_transform_point(msg, t)

            # self._object_pub.publish(ass)
            return True
        else:
            return False

    # For detecting the cube
    def detect_green(self, color, point, pointcloud):
        if color[0] < 0.2 and color[1] > 0.48 and color[2] > 0.4:   #RGB values of around (10,130,120)
            # t= TransformStamped()
            # #self.get_logger().info(f'Detected the green cube!')
            # t.transform.translation.x = float(point[0])
            # t.transform.translation.y = float(point[1])
            # t.transform.translation.z = float(point[2])
            # t.header.frame_id = 'camera_depth_optical_frame'
            # t.header.stamp = pointcloud.header.stamp
            # t.child_frame_id = '/object_position'
            # self._tf_broadcaster.sendTransform(t)
            return True
        else:
            return False
        
    def detect_brown(self, color, point, pointcloud):
        if color[0] > 0.55 and color[1] > 0.45 and color[2] < 0.35:   #RGB values of around (10,130,120)
            # t= TransformStamped()
            # #self.get_logger().info(f'Detected the brown thing!')
            # t.transform.translation.x = float(point[0])
            # t.transform.translation.y = float(point[1])
            # t.transform.translation.z = float(point[2])
            # t.header.frame_id = 'camera_depth_optical_frame'
            # t.header.stamp = pointcloud.header.stamp
            # t.child_frame_id = '/object_position'
            # self._tf_broadcaster.sendTransform(t)
            return True
        else:
            return False
    

        


def main():
    rclpy.init()
    node = Detection()
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
