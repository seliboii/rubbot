#!/usr/bin/env python

import rclpy
from rclpy.node import Node

from robp_interfaces.msg import DutyCycles


class OpenLoopController(Node):


    def __init__(self):
        super().__init__('open_loop_controller')
        
        # TODO: Implement
        self.publisher_ = self.create_publisher(DutyCycles, '/motor/duty_cycles', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = DutyCycles()
        msg.duty_cycle_left = 1.0
        msg.duty_cycle_right = 0.9
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)
        self.i += 1

        
   

def main():
    rclpy.init()
    node = OpenLoopController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()