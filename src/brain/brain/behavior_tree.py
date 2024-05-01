#!/usr/bin/env python

import rclpy
from rclpy.node import Node
import py_trees as pt
import py_trees_ros as ptr






class BehaviorTree(Node):

    def __init__(self):
        super().__init__('behavior_tree')
        


class BT(pt.behaviour.Behaviour):
    def __init__(self):
        tree = pt.composites.Sequence



        super(BT, self).__init__(tree)





def main():
    rclpy.init()
    node = BehaviorTree()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()