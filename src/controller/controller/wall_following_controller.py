#!/usr/bin/env python

import rclpy
from rclpy.node import Node

from robp_boot_camp_interfaces.msg import ADConverter
from geometry_msgs.msg import Twist
from math import exp, atan2,sqrt


class WallFollowingController(Node):

    def __init__(self):
        super().__init__('wall_following_controller')
        
        # TODO: Implement
        self.dt = 0.1
        self.d1 = 0.0
        self.d2 = 0.0
        self.l = 0.2
        self.theta = 0.0
        self.speed = 0.5
        self.kp = 0.6 
        self.adc_subscription = self.create_subscription(
            ADConverter,
            '/kobuki/adc',
            self.adc_callback,
            int(1/self.dt)
        )

        self.twist_publisher = self.create_publisher(
            Twist,
            '/motor_controller/twist',
            int(1/self.dt)
        )

        self.timer = self.create_timer(self.dt, self.twist_callback)
        
    # TODO: Implement
    
    def adc_callback(self, msg):
        self.d1 = 1.114*exp(-0.004*msg.ch1)
        self.d2 = 1.114*exp(-0.004*msg.ch2)
        # self.get_logger().info('d1: "%s"' % self.d1)
        self.theta = atan2(
            (self.d1 - self.d2),
            sqrt((self.d1 - self.d2) ** 2 + self.l ** 2)
        )
        self.get_logger().info('d1: "%s"' % self.theta)

    def twist_callback(self):
        twist_msg = Twist()
        twist_msg.linear.x = self.speed
        rotational_z = self.kp * self.theta
        if rotational_z > 1.0:
            twist_msg.angular.z = 1.0
        elif rotational_z < -1.0:
            twist_msg.angular.z = -1.0
        else:
            twist_msg.angular.z = rotational_z 
        self.twist_publisher.publish(twist_msg)
        self.get_logger().info('Wall following publishing: "%s"' %twist_msg)

def main():
    rclpy.init()
    node = WallFollowingController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()