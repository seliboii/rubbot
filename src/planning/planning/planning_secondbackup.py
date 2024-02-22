#!/usr/bin/env python

import math

import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2
from open3d import open3d as o3d
from geometry_msgs.msg import Twist, Pose
#ADD POSE MSG, NOT SURE IF CORRECT

import ctypes
import struct

class Planning(Node):

    def __init__(self):
        super().__init__('planning')
        # # Initialize the publisher
        self._twist_pub = self.create_publisher(Twist,'/motor_controller/twist', 10)

        self._goalpose_sub = self.create_subscription(Pose,'/object/position',self.object_callback,10)

        # # Subscribe to point cloud topic and call callback function on each recieved message
        # self.create_subscription(
        #     PointCloud2, '/camera/depth/color/points', self.cloud_callback, 10)
                                          
        #self._object_sub = self.create_subscription()

    def object_callback(self, msg:Pose):

        theta = np.arctan2(msg.position.x,msg.position.y)
        #theta = np.arctan2(msg.position.x,msg.position.z)
        msg2 = Twist()

        dist = np.sqrt(msg.position.x**2+msg.position.y**2)
       
        # if dist >= 0.25:
        #     msg2.linear.x = 0.4
        #     msg2.angular.z = -theta/10
        # else:
        #     msg2.linear.x = 0.0
        #     msg2.angular.z = 0.0
        
        if msg.position.z < 0.10:
            msg2.linear.x = 0.0
            msg2.angular.z = 0.0
            msg2.linear.y = 0.0
            msg2.linear.z = 0.0
            msg2.angular.x = 0.0
            msg2.angular.y = 0.0
            self.get_logger().info(f'{msg2.linear.x}, {msg.position.z} too close!')
            self._twist_pub.publish(msg2)

        else:
            msg2.linear.x = (msg.position.z)*0.5
            msg2.angular.z = -theta/5
            msg2.linear.y = 0.0
            msg2.linear.z = 0.0
            msg2.angular.x = 0.0
            msg2.angular.y = 0.0
            self.get_logger().info(f'{msg2.linear.x},{msg2.angular.z}')
            self._twist_pub.publish(msg2)
        
        #self._twist_pub.publish(msg2)

def main():
    rclpy.init()
    node = Planning()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()