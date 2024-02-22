#!/usr/bin/env python

import math

import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2
from open3d import open3d as o3d
from geometry_msgs.msg import Twist, Pose, PointStamped
import tf2_geometry_msgs
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from tf2_ros import TransformException
from std_msgs.msg import Bool
from aruco_msgs.msg import MarkerArray
#ADD POSE MSG, NOT SURE IF CORRECT


import ctypes
import struct

class Planning(Node):

    def __init__(self):
        super().__init__('planning')
        # # Initialize the publisher
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self._twist_pub = self.create_publisher(Twist,'/motor_controller/twist', 10)

        self._goalpose_sub = self.create_subscription(PointStamped,'/object/position',self.object_callback,10)

        #self._aruco_sub = self.create_subscription(MarkerArray,'/marker_publisher/markers',self.aruco_callback,10)

        self.status_pub = self.create_publisher(Bool, '/planning/status', 10)

        self.trigger_sub = self.create_subscription(
            Bool,
            '/planning/switch',
            self.switch_callback,
            10
        )       


        # # Subscribe to point cloud topic and call callback function on each recieved message
        # self.create_subscription(
        #     PointCloud2, '/camera/depth/color/points', self.cloud_callback, 10)
                                          
        #self._object_sub = self.create_subscription()
        self.dt = 0.1
        self.timer = self.create_timer(self.dt, self.on_timer)
        self.latest_x = 1.0
        self.latest_y = 1.0
        self.latest_z = 1.0
        self.int_error = 0.0
        self.switch = False

        
    def switch_callback(self, msg: Bool):
        if msg.data:
            self.switch = True
        else:
            self.switch = False

    
    def object_callback(self, msg:PointStamped):
        

        try:
            t = self.tf_buffer.lookup_transform(
                'map',
                'camera_depth_optical_frame',
                msg.header.stamp,   #TODO fix timestamping
                timeout=rclpy.duration.Duration(seconds=0.2)
                )
        except TransformException as ex:
            self.get_logger().info(
                f'could not transform: {ex}')
            
            return
        self.latest_x = msg.point.x
        self.latest_y = msg.point.y
        self.latest_z = msg.point.z

        p = tf2_geometry_msgs.do_transform_point(msg, t)

       
    

    # def aruco_callback(self, msg):
        

    #     # try:
    #     #     t = self.tf_buffer.lookup_transform(
    #     #         'base_link',
    #     #         'map',
    #     #         rclpy.time.Time(),   #TODO fix timestamping
    #     #         timeout=rclpy.duration.Duration(seconds=0.2)
    #     #         )
            

    #     # except TransformException as ex:
    #     #     self.get_logger().info(
    #     #         f'could not transform: {ex}')
            
    #     #     return

    #     #p = tf2_geometry_msgs.do_transform_point(msg, t)

    #     if len(msg.markers) > 0:
    #         latest_marker_pose = msg.markers[-1].pose.pose  
    #         self.latest_x = latest_marker_pose.position.x  
    #         self.latest_y = latest_marker_pose.position.y  
    #         self.latest_z = latest_marker_pose.position.z  



    def on_timer(self):

        if self.switch:


            self.get_logger().info(f"x = {self.latest_x}")

            self.get_logger().info(f"y = {self.latest_y}")

            self.get_logger().info(f"z = {self.latest_z}")

            alpha = 1
            beta = 0.01

            error = -np.arctan2(self.latest_x,self.latest_z)
            self.int_error += error*self.dt
            angular_vel = error*alpha#+self.int_error*beta
            
            #dist = np.sqrt(self.latest_x**2+self.latest_y**2)

            dist = self.latest_z

            self.get_logger().info(f"distance = {dist}")
 
            msg2 = Twist()

            status = Bool()
            status.data = True

            #self.get_logger().info(f"messgae = {dist}")

            
            if dist >0.3:
                msg2.linear.x = 0.3
                msg2.angular.z = angular_vel/4
                status.data = True
                self.status_pub.publish(status)
            elif dist <0.3:
                msg2.linear.x = 0.0
                msg2.angular.z = 0.0
                status.data = False
                self.status_pub.publish(status)
            else:
                status.data = True
                self.status_pub.publish(status)
            
            msg2.linear.y = 0.0
            msg2.linear.z = 0.0
            msg2.angular.x = 0.0
            msg2.angular.y = 0.0

            self._twist_pub.publish(msg2)

    
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