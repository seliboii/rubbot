#!/usr/bin/env python

import rclpy
from rclpy.node import Node


class StateMachine(Node):
    def __init__(self):
        super().__init__('test_statemachine')

        sm_period = 0.1
        self.state = 'init'
        self.create_timer(sm_period, self.sm_cb)

    def sm_cb(self):
        match self.state:
            case 'init':
                self.get_logger().info('In init state')
                self.state = 'next_state'
            case _:
                self.get_logger().info('In default state')


def main():
    rclpy.init()
    node = StateMachine()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()