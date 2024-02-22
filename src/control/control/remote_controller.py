#!/usr/bin/env python

import rclpy
from rclpy.node import Node

from robp_interfaces.msg import DutyCycles
from sensor_msgs.msg import Joy


class remote_controller(Node):

    def __init__(self):
        super().__init__('remote_controller')
        
        self.Joy_sub = self.create_subscription(
            Joy,
            '/joy',
            self.joy_callback,
            10
        )

        self.dutycycles_pub = self.create_publisher(
            DutyCycles,
            '/motor/duty_cycles',
            10
        )

        self.timer = self.create_timer(0.5, self.dutycycles_callback)

        self.left = 0.0
        self.right = 0.0
        
    def joy_callback(self,msg):
        foward = (msg.axes[5] - 1) / -2
        backward = (msg.axes[2] - 1 ) / -2
        turn = (msg.axes[3])
        self.left = (foward - backward) * 0.25 - turn * 0.25
        self.right = (foward - backward) * 0.25 + turn * 0.25

    def dutycycles_callback(self):
        msg = DutyCycles()
        left_w = self.left
        right_w = self.right
        msg.duty_cycle_left = left_w
        msg.duty_cycle_right = right_w
        self.dutycycles_pub.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)

def main():
    rclpy.init()
    node = remote_controller()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()