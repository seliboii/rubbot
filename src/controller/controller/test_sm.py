#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Twist, PointStamped
import rclpy.time
import rclpy.waitable
from rubbot_interfaces.msg import GoalReached
from std_msgs.msg import String, Bool
import time
from nav_msgs.msg import Path, OccupancyGrid
from tf_transformations import euler_from_quaternion, quaternion_from_euler
import math
import numpy as np
from io import BytesIO
from pygame import mixer
from gtts import gTTS
import playsound
import os
import time
from robp_interfaces.msg import Information

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
        
        self.explore_goal = self.create_publisher(
            PointStamped,
            '/explore/position',
            1
        )

        self.arm_feedback_update = self.create_publisher(
            Bool,
            '/state_machine/arm',
            10
        )

        self.odometry_update = self.create_subscription(
            Path, 
            '/path',
            self.odom_cb, 
            1
        )

        self.map_update = self.create_subscription(
            OccupancyGrid, 
            '/occupancy_grid',
            self.map_cb, 
            1
        )
       
        self.obstacle_sub = self.create_subscription(
            Information,
            '/object_og', 
            self.detected_object_callback,
            1
        )
        
        self.get_aruco_pose = self.create_subscription(
            Information,
            '/marker_publisher/pose',
            self.detected_aurco_callback,
            1
            )


        self.goalpose = PoseStamped()
        # test goalpose
        self.goalpose.pose.position.x = 0.0
        self.goalpose.pose.position.y = 0.0
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
        self.goal_reached = True

        self.first_iter =True
        self.odom_x = 0  
        self.odom_y = 0
        self.odom_theta = 0
        self.test_stamp = 0
        self.explored_layer = -4 

        self.object_list = []
        self.aruco_list = []

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
                self.state = 'pick'
                self.speak_bitch(" jejejej   we are now rotating")

            case 'rotate':
                max_cnt = 14
                self.twist.angular.z = 1.5
                if abs(self.cnt) < max_cnt:
                    self.twist_pub.publish(self.twist)
                    self.cnt += 1
                    return
                elif self.cnt % max_cnt == 0:
                    self.twist.angular.z = 0.0
                    self.twist_pub.publish(self.twist)
                    print("SLEEPING")
                    time.sleep(2)
                    self.cnt += 1
                    return
                elif max_cnt <= self.cnt < 2*max_cnt:
                    self.twist_pub.publish(self.twist)
                    self.cnt += 1
                    return
                elif 2*max_cnt <= self.cnt < 3*max_cnt:
                    self.twist_pub.publish(self.twist)
                    self.cnt += 1
                    return
                elif 3*max_cnt <= self.cnt < 4*max_cnt:
                    self.twist_pub.publish(self.twist)
                    self.cnt += 1
                    return
                elif 4*max_cnt <= self.cnt < 5*max_cnt:
                    self.twist_pub.publish(self.twist)
                    self.cnt += 1
                    return
                self.cnt = -1
                self.twist.angular.z = 0.0
                self.twist_pub.publish(self.twist)
                self.state = 'explore'
                self.speak_bitch("yoooooooooo we are now exploring viva españa viva el rey viva el orden y la ley")

            case 'explore':
                max_cnt = 20
                # print("COUNTER: ", self.cnt)
                # print("GOAL REACH: ", self.goal_reached)
                if self.cnt < max_cnt:
                    if self.goal_reached:
                        print("LAYERS: ", self.explored_layer)
                        x, y = edging(self.data,self.res, self.explored_layer)
                        self.explored_layer = y
                        test = PointStamped()
                        test.point.x = x
                        test.point.y = y
                        test.header.frame_id = 'map'
                        test.header.stamp = self.test_stamp
                        self.explore_goal.publish(test)
                        print("X: ",x," Y: ", y)
                        self.goalpose.pose.position.x = x
                        self.goalpose.pose.position.y = y
                        self.goalpub.publish(self.goalpose)
                        self.goal_reached = False
                        self.cnt += 1
                else:
                    print("FINISHED EXPLORED")
                    self.speak_bitch("          We have finished exploring. Viva España, Viva el rey. Viva el orden Y la ley")
                    self.state = 'pick'
                    
            case 'goto_object':
                
                if self.first_iter:
                    goal_object = self.object_list[-1]
                    goal_x = goal_object[1].pose.position.x
                    goal_y = goal_object[1].pose.position.y
                    self.goalpose.pose.position.x = goal_x
                    self.goalpose.pose.position.y = goal_y
                    self.goalpub.publish(self.goalpose)
                    self.goal_reached = False
                    self.first_iter = False
                    print("GOING TO OBJECT")
                elif self.goal_reached:
                    self.first_iter = True
                    print("GOING TO Pick")
                    self.state = 'pick'


            case 'send2goal':
                if self.first_iter:
                    self.goalpub.publish(self.goalpose)
                    self.first_iter = False
                if self.goal_reached:
                    print("HEREEEEEEEEEEEEe")
                    self.state = 'pick'
                    self.first_iter = True
                else:
                    print("guh")
            
            case 'pick':
                if self.first_iter:
                    self.arm_string.data = 'pick'
                    self.arm_pub.publish(self.arm_string)
                    self.arm_pub.publish(self.arm_string)
                    self.arm_pub.publish(self.arm_string)
                else:
                    print("puh")
            case _:
                self.get_logger().info('In default state')

    def goal_cb(self, msg):
        self.goal_reached = msg

    def map_cb(self, msg: OccupancyGrid):
        self.data = np.reshape(msg.data,(msg.info.height,msg.info.width))
        self.res = msg.info.resolution 
        self.test_stamp = msg.header.stamp   

    def odom_cb(self, msg: Path):
        self.odom_x = msg.poses[0].pose.position.x
        self.odom_y = msg.poses[0].pose.position.x
        msg.poses[0].pose.orientation.y
        msg.poses[0].pose.orientation.z
        msg.poses[0].pose.orientation.w

        q = euler_from_quaternion(
            [msg.poses[0].pose.orientation.x,
             msg.poses[0].pose.orientation.y,
             msg.poses[0].pose.orientation.z,
             msg.poses[0].pose.orientation.w]
            )
        self.odom_theta = q[2]

    def arm_feedback_callback(self, msg):
        if msg.data:
            self.first_iter = False
            arm_sm_update = Bool()
            arm_sm_update.data = False
            self.arm_feedback_update.publish(arm_sm_update)

    def speak_bitch(self, text):
        time.sleep(2)
        tts = gTTS(text = text, lang = 'es')
        filename = "textfile.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    def detected_aurco_callback(self, msg: Information):
        DISTANCE_THRESHOLD = 0.1 #meter
        new_id = msg.label
        new_pose = msg.pose

        #object_list [label, PoseStamped]

        for object in self.aruco_list:
            if object[0] == new_id:
                old_x = object[1].pose.position.x
                old_y = object[1].pose.position.y
                new_x = new_pose.pose.position.x
                new_y = new_pose.pose.position.y
                dist = math.dist([old_y, old_x], [new_y, new_x])
                if dist < DISTANCE_THRESHOLD:
                    return
        DISTANCE_INFRONT = 0.2 #METERS
        e = euler_from_quaternion([
            new_pose.pose.orientation.x,
            new_pose.pose.orientation.y,
            new_pose.pose.orientation.z,
            new_pose.pose.orientation.w
        ])
        new_pose.pose.position.x = new_pose.pose.position.x + math.cos(e[2]) * DISTANCE_INFRONT 
        new_pose.pose.position.y = new_pose.pose.position.y + math.sin(e[2]) * DISTANCE_INFRONT
        
        q = quaternion_from_euler(0,0,e[2]+math.pi)
        new_pose.pose.orientation.x = q[0]
        new_pose.pose.orientation.y = q[1]
        new_pose.pose.orientation.z = q[2]
        new_pose.pose.orientation.w = q[3]

        self.aruco_list.append([new_id, new_pose])

    def detected_object_callback(self, msg: Information):
        DISTANCE_THRESHOLD = 0.1 #meter
        new_label = msg.label
        new_pose = msg.pose

        #object_list [label, PoseStamped]

        for object in self.object_list:
            if object[0] == new_label:
                old_x = object[1].pose.position.x
                old_y = object[1].pose.position.y
                new_x = new_pose.pose.position.x
                new_y = new_pose.pose.position.y
                dist = math.dist([old_y, old_x], [new_y, new_x])
                if dist < DISTANCE_THRESHOLD:
                    return
        self.object_list.append([new_label, new_pose])
        
        print("OBEJCT LIST: ", self.object_list)



def edging(data, res, layer):
    min_y = int((layer+2)/res)
    print("MIN_y", min_y)
    h, w = data.shape
    for x in range(h):
        for y in range(min_y, w):
            if data[x][y] != 0:
                pass
            else:
                if data[x-1][y] == -1 or data[x+1][y] == -1 or data[x][y+1] == -1 or data[x][y-1] == -1:
                    scaled_x = res*y-4
                    scaled_y = res*x-2
                    return float(scaled_x), float(scaled_y) 
    print("I FUCKED UP")
    
    





    
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