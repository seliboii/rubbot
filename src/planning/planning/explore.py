#!/usr/bin/env python

import rclpy
from rclpy.node import Node

from robp_interfaces.msg import DutyCycles, Encoders
from geometry_msgs.msg import Twist
from nav_msgs.msg import OccupancyGrid


class Explorer(Node):

    def __init__(self):
        super().__init__('explorer')
        
        self.map_update = self.create_subscription(
            OccupancyGrid, 
            '/occupancy_grid',
            self.map_cb, 
            1
        )
        
    


def main():
    rclpy.init()
    node = Explorer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()