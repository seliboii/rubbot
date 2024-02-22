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
from geometry_msgs.msg import TransformStamped, Pose


class Detection(Node):

    def __init__(self):
        super().__init__('detection')

        # Subscribe to the original pointcloud
        self.create_subscription(PointCloud2, '/camera/depth/color/points', self.cloud_callback, 10)

        # Initialize the publisher of our filtered pointcloud
        self._pub = self.create_publisher(PointCloud2, '/camera/depth/color/ds_points', 10)

        self._object_pub = self.create_publisher(Pose,'/object/position',10)        


        # Initialize the transform broadcaster
        self._tf_broadcaster = TransformBroadcaster(self)


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
        distance_threshold = 1.6

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
        if color[0] > 0.5 and color[1] < 0.4 and color[2] < 0.4:  #if color[0] > 0.5 and color[1] < 0.4 and color[2] < 0.4:
            t= TransformStamped()
            #self.get_logger().info(f'Detected the red ball!')
            t.transform.translation.x = float(point[0])
            t.transform.translation.y = float(point[1])
            t.transform.translation.z = float(point[2])
            t.header.frame_id = 'camera_depth_optical_frame'
            t.header.stamp = pointcloud.header.stamp
            t.child_frame_id = '/object_position'
            self._tf_broadcaster.sendTransform(t)
            msg = Pose()
            msg.position.x = t.transform.translation.x
            msg.position.y = t.transform.translation.y
            msg.position.z = t.transform.translation.z
            msg.orientation.x = 0.0
            msg.orientation.y = 0.0
            msg.orientation.z = 0.0
            msg.orientation.w = 1.0
            self._object_pub.publish(msg)

            return True
        else:
            return False

    # For detecting the cube
    def detect_green(self, color, point, pointcloud):
        if color[0] < 0.2 and color[1] > 0.48 and color[2] > 0.4:   #RGB values of around (10,130,120)
            t= TransformStamped()
            #self.get_logger().info(f'Detected the green cube!')
            t.transform.translation.x = float(point[0])
            t.transform.translation.y = float(point[1])
            t.transform.translation.z = float(point[2])
            t.header.frame_id = 'camera_depth_optical_frame'
            t.header.stamp = pointcloud.header.stamp
            t.child_frame_id = '/object_position'
            self._tf_broadcaster.sendTransform(t)
            return True
        else:
            return False
        
    def detect_brown(self, color, point, pointcloud):
        if color[0] > 0.55 and color[1] > 0.45 and color[2] < 0.35:   #RGB values of around (10,130,120)
            t= TransformStamped()
            #self.get_logger().info(f'Detected the brown thing!')
            t.transform.translation.x = float(point[0])
            t.transform.translation.y = float(point[1])
            t.transform.translation.z = float(point[2])
            t.header.frame_id = 'camera_depth_optical_frame'
            t.header.stamp = pointcloud.header.stamp
            t.child_frame_id = '/object_position'
            self._tf_broadcaster.sendTransform(t)
            return True
        else:
            return False


def main():
    rclpy.init()
    node = Detection()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()
