#!/usr/bin/env python

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16MultiArray, Bool


class ArmControl(Node):

    def __init__(self):
        super().__init__('arm_control')
        
        self.pos_sub = self.create_subscription(
            Int16MultiArray,
            '/arm/arm_pose',
            self.pos_callback,
            10
        )

        self.arm_move_pub = self.create_publisher(
            Int16MultiArray,
            '/multi_servo_cmd_sub',
            10
        )

        self.pos_pub = self.create_publisher(
            Int16MultiArray,
            '/arm/arm_pose',
            10
        )

        self.robstate_pub = self.create_publisher(
            Bool,
            '/arm/work_state',
            10
        )

        self.timer = self.create_timer(0.1, self.arm_callback)

        self.act = 0
        self.s6 = 0
        self.s5 = 0
        self.s4 = 0
        self.s3 = 0
        self.count = 0
    
    def working(self):
        msg = Bool()
        msg.data = True
        self.robstate_pub.publish(msg)

    def notworking(self):
        msg = Bool()
        msg.data = False
        self.robstate_pub.publish(msg)

    def pos_callback(self,msg):
        if msg.data[0] != 0:
            self.act = msg.data[0]
            self.s6 = msg.data[1]
            self.s5 = msg.data[2]
            self.s4 = msg.data[3]
            self.s3 = msg.data[4]
            msg = Int16MultiArray()
            msg.data = [0, 0, 0, 0, 0]
            self.count = 0
            self.pos_pub.publish(msg)

    def arm_callback(self):
        arm_msg = Int16MultiArray()
        if self.act == 1:
            if self.count == 0:
                arm_msg.data = [2000, 12000, self.s3, self.s4, 12000, self.s6, 1000, 1000, 1000, 1000, 1000, 1000]
                self.arm_move_pub.publish(arm_msg)
                self.working()
                self.count += 1
            elif self.count == 20:
                arm_msg.data = [-1, -1, -1, -1, self.s5, -1, 1000, 1000, 1000, 1000, 1000, 1000]
                self.arm_move_pub.publish(arm_msg)
                self.working()
                self.count += 1
            elif self.count ==  40:
                arm_msg.data = [11000, 12000, -1, -1, -1, -1, 1000, 1000, 1000, 1000, 1000, 1000]
                self.arm_move_pub.publish(arm_msg)
                self.working()
                self.count += 1
            elif self.count ==  60:
                arm_msg.data = [11000, 12000, 12000, 12000, 12000, 12000, 1000, 1000, 1000, 1000, 1000, 1000]
                self.arm_move_pub.publish(arm_msg)
                self.working()
                self.count += 1
            elif self.count == 75:
                self.notworking()
                self.count = 0
                self.act = 0
            else:
                self.count += 1
                self.working()
        elif self.act == 2:
            if self.count == 0:
                arm_msg.data = [-1, 12000, self.s3, self.s4, self.s5, self.s6, 1000, 1000, 1000, 1000, 1000, 1000]
                self.arm_move_pub.publish(arm_msg)
                self.working()
                self.count += 1
            elif self.count == 20:
                arm_msg.data = [2000, 12000, self.s3, self.s4, self.s5, self.s6, 1000, 1000, 1000, 1000, 1000, 1000]
                self.arm_move_pub.publish(arm_msg)
                self.working()
                self.count += 1
            elif self.count ==  40:
                arm_msg.data = [2000, 12000, 12000, 12000, 12000, 12000, 1000, 1000, 1000, 1000, 1000, 1000]
                self.arm_move_pub.publish(arm_msg)
                self.working()
                self.count += 1
            elif self.count == 55:
                self.notworking()
                self.count = 0
                self.act = 0
            else:
                self.count += 1
                self.working()
        else:
            self.notworking()





def main():
    rclpy.init()
    node = ArmControl()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()