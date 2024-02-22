#!/usr/bin/env python

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16MultiArray
from sensor_msgs.msg import Joy

class arm_controller(Node):

    def __init__(self):
        super().__init__('arm_controller')

        self.joy_subscription = self.create_subscription(
            Joy,
            '/joy',
            self.joy_callback,
            10)
        
        self.arm_publisher = self.create_publisher(
            Int16MultiArray,
            '/multi_servo_cmd_sub',
            20
        )

        self.timer = self.create_timer(0.05, self.arm_callback)

        self.s1 = 12000
        self.s2 = 12000
        self.s3 = 12000
        self.s4 = 12000
        self.s5 = 12000
        self.s6 = 12000
        self.t1 = 100
        self.t2 = 100
        self.t3 = 100
        self.t4 = 100
        self.t5 = 100
        self.t6 = 100

        self.d = 200
        self.c = 400

    def joy_callback(self,msg):

        if msg.buttons[7] == 1:
            if self.s1 + self.c > 12000:
                self.s1 = 12000
            else:
                self.s1 += self.c

        if msg.buttons[6] == 1:
            if self.s1 - self.c< 0:
                self.s1 = 0
            else:
                self.s1 -= self.c
            
        if msg.buttons[5] == 1:
            if self.s6 + self.d > 24000:
                self.s6 = 24000
            else:
                self.s6 += self.d

        if msg.buttons[4] == 1:
            if self.s6 - self.d < 0:
                self.s6 = 0
            else:
                self.s6 -= self.d

        if msg.buttons[2] == 1:
            if self.s2 + self.d > 24000:
                self.s2 = 24000
            else:
                self.s2 += self.d

        if msg.buttons[0] == 1:
            if self.s2 - self.d < 0:
                self.s2 = 0
            else:
                self.s2 -= self.d

        if msg.buttons[3] == 1:
            if self.s3 + self.d > 24000:
                self.s3 = 24000
            else:
                self.s3 += self.d

        if msg.buttons[1] == 1:
            if self.s3 - self.d < 0:
                self.s3 = 0
            else:
                self.s3 -= self.d

        if msg.axes[4] < 0:
            if self.s4 + self.d > 24000:
                self.s4 = 24000
            else:
                self.s4 += self.d 
        elif msg.axes[4] > 0:
            if self.s4 - self.d < 0:
                self.s4 = 0
            else:
                self.s4 -= self.d 

        if msg.axes[5] > 0:
            if self.s5 + self.d > 24000:
                self.s5 = 24000
            else:
                self.s5 += self.d 
        elif msg.axes[5] < 0:
            if self.s5 - self.d < 0:
                self.s5 = 0
            else:
                self.s5 -= self.d 

    def arm_callback(self):
        msg = Int16MultiArray()

        data_arm = [self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.t1, self.t2, self.t3, self.t4, self.t5, self.t6]

        msg.data = data_arm

        self.arm_publisher.publish(msg)
        self.get_logger().info('Arm: "%s"' %msg)


        

        



def main():
    rclpy.init()
    node = arm_controller()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()
