#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Twist
import rclpy.waitable
from rubbot_interfaces.msg import GoalReached


class StateMachine(Node):
    def __init__(self):
        super().__init__('test_statemachine')

        sm_period = 0.1
        self.state = 'init'
        self.create_timer(sm_period, self.sm_cb)
        self.twist_pub = self.create_publisher(
            Twist,
            '/motor_controller/twist',
            1
        )
        self.goalpose = PoseStamped()
        # test goalpose
        self.goalpose.pose.position.x = -1.0
        self.goalpose.pose.position.y = 3.0
        self.twist = Twist()
        self.cnt = 0
        # self.goalpose.pose.position.x = 5

        # Publisher for goal
        self.goalpub = self.create_publisher(
            PoseStamped,
            '/move_base/goal',
            1
        )
        self.create_subscription(GoalReached, '/goal/status', self.goal_cb, 1)
        # self.goal_reached = GoalReached()
        self.goal_reached = False


    def sm_cb(self):
        match self.state:
            case 'init':
                self.get_logger().info('In init state')
                self.state = 'rotate'
            case 'rotate':
                self.twist.angular.z = 1.5
                if self.cnt < 10:
                    self.twist_pub.publish(self.twist)
                    self.cnt += 1
                    return
                    
                self.twist.angular.z = 0.0
                self.twist_pub.publish(self.twist)
                self.state = 'send2goal'
            case 'send2goal':

                self.goalpub.publish(self.goalpose)
                if self.goal_reached:
                    self.state = 'escape'
                else:
                    print("guh")

            case _:
                self.get_logger().info('In default state')

    def goal_cb(self, msg):
        self.goal_reached = msg
    
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