#!/usr/bin/env python

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16MultiArray, Float32MultiArray
from robp_interfaces.msg import ObjPos
from math import sin, cos, acos, asin, atan2, pi
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Point


class ARM_FK(Node):

    def __init__(self):
        super().__init__('arm_fk')

        self.obj_pub = self.create_publisher(
            ObjPos,
            '/arm/object', #An object position in form of [activation,x,y]
            10
        )

        self.arm_pos_sub = self.create_subscription(
            JointState,
            '/servo_pos_publisher', #An pose with position for servo 3, 4, 5, 6, and conformation of activation
            self.cam_pos_callback, 
            10
        )

        self.fk_sub = self.create_subscription(
            Float32MultiArray,
            '/arm/forward_kinematic', #An pose with position for servo 3, 4, 5, 6, and conformation of activation
            self.state_machine_callback,
            10
        )

        self.fk_pub = self.create_publisher(
            Float32MultiArray,
            '/arm/forward_kinematic', #An pose with position for servo 3, 4, 5, 6, and conformation of activation
            10
        )

        self.obj_pos_to_statemachine_pub = self.create_publisher(
            Float32MultiArray,
            '/arm_state/obj_pos',
            10
        )

        

        
        self.l1 = 0.101
        self.l2 = 0.094
        self.l3 = 0.169
        self.l_camera = 0.045
        self.base_height = 0.135
        self.x_from_base = 0.0
        self.y_from_base = 0.0
        self.x = 0.0
        self.y = 0.0
        self.active = 0.0
        self.box = 0.1

    def cam_pos_callback(self,msg):
        s1 = float(msg.position[0])/18000.0*pi
        s2 = float(12000-msg.position[1])/18000.0*pi
        s3 = float(12000-msg.position[2])/18000.0*pi
        s4 = float(12000-msg.position[3])/18000.0*pi
        s5 = float(msg.position[4])/18000.0*pi
        s6 = float(msg.position[5])/18000.0*pi
        self.x = sin(s2) * self.l1 + sin(s2+s3) * self.l2 + sin(s2 + s3 + s4) * self.l3 + sin(s2 + s3 + s4 - pi/2) * self.l_camera
        self.y = 0


    
    def state_machine_callback(self, msg):
        if msg.data[0] == 1:
            self.x = self.x + msg.data[2]
            self.y = self.y - msg.data[1]
            obj_pos_msg = Float32MultiArray()
            obj_pos_msg.data = [1.0, self.x, self.y]
            self.obj_pos_to_statemachine_pub.publish(obj_pos_msg)
            fk_msg = Float32MultiArray()
            fk_msg.data = [0.0, 0.0, 0.0]
            print(obj_pos_msg)
            self.fk_pub.publish(fk_msg)




def main():
    rclpy.init()
    node = ARM_FK()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()