#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Twist
import rclpy.waitable
from rubbot_interfaces.msg import GoalReached
from std_msgs.msg import String, Bool


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
        self.arm_feedback = self.create_subscription(
            Bool,
            '/state_machine/arm',
            self.arm_feedback_callback,
            10
        )
        self.arm_feedback_update = self.create_publisher(
            Bool,
            '/state_machine/arm',
            10
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

        self.first_iter =True

        # publish arm actions
        self.arm_pub = self.create_publisher(
            String,
            '/arm/state_machine',
            1
        )
        self.arm_string = String()

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
                if self.first_iter:
                    self.goalpub.publish(self.goalpose)
                    self.first_iter = False
                if self.goal_reached:
                    self.state = 'pick'
                    self.first_iter = True
                else:
                    print("guh")
            
            case 'pick':
                if self.first_iter:
                    self.arm_string.data = 'pick'
                    self.arm_pub.publish(self.arm_string)
                else:
                    print("puh")
            case _:
                self.get_logger().info('In default state')

    def goal_cb(self, msg):
        self.goal_reached = msg

    def arm_feedback_callback(self, msg):
        if msg.data:
            self.first_iter = False
            arm_sm_update = Bool()
            arm_sm_update = False
            self.arm_feedback_update.publish(arm_sm_update)


    
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