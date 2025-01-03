#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action.server import ServerGoalHandle
from rclpy.action.client import ClientGoalHandle
from rubbot_interfaces.action import MoveToGoal
from rubbot_interfaces.msg import GoalReached
from geometry_msgs.msg import PoseStamped
from robp_interfaces.msg import Information
from tf_transformations import quaternion_from_euler, euler_from_quaternion

class MoveToGoalClientNode(Node):
    def __init__(self):
        super().__init__("move_to_goal_client")
        self.move_to_goal_client = ActionClient(
            self,
            MoveToGoal,
            "move_to_goal")
        # Subscription for rviz goal controller
        # self._get_goal = self.create_subscription(PoseStamped, '/move_base_simple/goal',self.goal_callback,10)
        # Subscription for general goal controller
        self._get_goal = self.create_subscription(Information, '/move_base/goal',self.goal_callback,10)
        self.msg_pub = self.create_publisher(GoalReached,
                              '/goal/status',
                              1)
        
    
    def goal_callback(self,msg: Information):
        goal_x = msg.pose.pose.position.x
        goal_y = msg.pose.pose.position.y
        e = euler_from_quaternion([
            msg.pose.pose.orientation.x,
            msg.pose.pose.orientation.y,
            msg.pose.pose.orientation.z,
            msg.pose.pose.orientation.w

        ])
        goal_theta = e[2]
        goal_type = msg.label
        self.send_goal(goal_x,goal_y,goal_theta,goal_type,0.0)
        
        
    def send_goal(self,x,y,theta,type,max_period):
        self.move_to_goal_client.wait_for_server()
        
        #create a goal

        goal = MoveToGoal.Goal()
        goal.x = x
        goal.y = y
        goal.max_period = max_period
        goal.angular_z = theta
        goal.type = type

        #send goal
        self.get_logger().info("Sending goal")
        self.move_to_goal_client.send_goal_async(goal).add_done_callback(self.goal_response_callback)
    
    def goal_response_callback(self, future):#IF the goal is accepcted or not
        self.goal_handle: ClientGoalHandle = future.result()
        if self.goal_handle.accepted:
            self.goal_handle.get_result_async().add_done_callback(self.goal_result_callback)

    def goal_result_callback(self, future): #Return the result
        result = future.result().result
        self.get_logger().info("Result: "+str(result.reached_goal))
        result_msg = GoalReached()
        result_msg.goal_reached = result.reached_goal
        self.msg_pub.publish(result_msg)
            


        
        


def main(args=None):
    rclpy.init(args=args)
    node = MoveToGoalClientNode()
    #node.send_goal(3.0,0.0,0.0)
    rclpy.spin(node)
    rclpy.shutdown()



if __name__ == "__main__":
    main()