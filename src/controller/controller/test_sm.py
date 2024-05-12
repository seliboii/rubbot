#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Twist, PointStamped, Pose
import rclpy.time
import rclpy.waitable
from rubbot_interfaces.msg import GoalReached
from std_msgs.msg import String, Bool
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
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
from math import atan2

class StateMachine(Node):
    def __init__(self):
        super().__init__('test_statemachine')
        cbg = ReentrantCallbackGroup()

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
            10,
            callback_group=cbg
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
            1,
            callback_group=cbg
        )

        self.map_update = self.create_subscription(
            OccupancyGrid, 
            '/occupancy_grid',
            self.map_cb, 
            1,
            callback_group=cbg
        )
       
        self.obstacle_sub = self.create_subscription(
            Information,
            '/object_og', 
            self.detected_object_callback,
            1,
            callback_group=cbg
        )
        
        self.get_aruco_pose = self.create_subscription(
            Information,
            '/marker_publisher/pose',
            self.detected_aurco_callback,
            1,
            callback_group=cbg
            )
        
        self.create_subscription(
            Pose, '/marker_publisher/feedbackpose', self.fb_cb, 1
        )

        self.feedback_obj_pose = Pose()
        self.approach_pose = Pose()

        self.acc_err = 0
        
        self.temp_pub = self.create_publisher(
            PoseStamped,
            '/temp/display_pose',
            1
        )




        self.goalpose = Information()
        # test goalpose
        # self.goalpose.pose.pose.position.x = 0.0
        # self.goalpose.pose.pose.position.y = 0.0
        self.twist = Twist()
        self.cnt = 0
        # self.goalpose.pose.position.x = 5

        # Publisher for goal
        self.goalpub = self.create_publisher(
            Information,
            '/move_base/goal',
            1
        )
        self.create_subscription(GoalReached, '/goal/status', self.goal_cb, 1, callback_group=cbg)
        # self.goal_reached = GoalReached()
        self.goal_reached = True

        self.first_iter =True
        self.odom_x = 0  
        self.odom_y = 0
        self.odom_theta = 0
        self.test_stamp = 0
        self.explored_layery = -2 
        self.explored_layerx = -4

        self.object_list = []
        self.aruco_list = []

        #ros2 topic pub /marker_publisher/pose robp_interfaces/msg/Information "{pose: {header: {stamp: {sec: 0, nanosec: 0}, frame_id: 'map'}, pose: {position: {x: 1.0, y: 0.5, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.707, w: 0.707}}}, label: 'box'}"



        # publish arm actions
        self.arm_pub = self.create_publisher(
            String,
            '/arm/state_machine',
            1
        )
        self.arm_string = String()

    def sm_cb(self):
        match self.state:
            case 'wait':
                if self.cnt > 10:
                    self.state = 'approach'
                self.cnt += 1

            # approach rotates until it is directly facing (withing margin) an object (currently it only handles aruco markers), 
            # then open loop drives forward for a fixed time, fixed velocity 
            case 'approach':
                if self.first_iter:
                    # self.approach_pose = self.feedback_obj_pose
                    self.first_iter = False

                # x_error = self.approach_pose.position.x - self.odom_x #self.feedback_obj_pose
                # y_error = self.approach_pose.position.y - self.odom_y
                
                if abs(self.feedback_obj_pose.position.x) > 0.1:
                    self.twist.linear.x = 0.0
                    self.twist.angular.z = -10 * self.feedback_obj_pose.position.x
                    print('x offset :', self.feedback_obj_pose.position.x)
                
                else:
                    self.twist.angular.z = 0.0
                    self.twist.linear.x = 0.0
                    self.cnt += 1

                if self.cnt > 50:
                    self.twist.angular.z = 0.0
                    self.twist.linear.x = 0.0
                    self.state = 'out'
                    self.first_iter = True

                # phi = atan2(y_error, x_error)
                # theta_error = phi - self.odom_theta

                # dist = y_error**2 + x_error**2

                # self.acc_err += theta_error
                # self.twist.angular.z = 5 * theta_error #+ 1 * self.acc_err
                # self.twist.linear.x = 1 * dist

                # print('theta err: ', theta_error, ' distance: ', dist)

                self.twist_pub.publish(self.twist)

            case 'init':
                self.get_logger().info('In init state')
                self.state = 'rotate'
                self.speak_bitch(" jejejej   we are now rotating")

            case 'rotate':
                # print(self.data.shape)
                # print(self.data[800][:])

                max_cnt = 40
                self.twist.angular.z = 1.4
                if abs(self.cnt) < max_cnt:
                    self.twist_pub.publish(self.twist)
                    self.cnt += 1
                    return
                elif self.cnt % max_cnt == 0:
                    self.twist.angular.z = 0.0
                    self.twist_pub.publish(self.twist)
                    print("SLEEPING")
                    #time.sleep(2)
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
                self.get_logger().info('Going to explore')
                self.speak_bitch("yoooooooooo we are now exploring")

            case 'explore':
                max_cnt = 20
                # print("COUNTER: ", self.cnt)
                # print("GOAL REACH: ", self.goal_reached)
                if self.cnt < max_cnt:
                    if self.goal_reached:
                        #print("LAYERS: ", self.explored_layery)
                        x, y = edging(self.data,self.res, self.explored_layery, self.explored_layerx)
                        self.explored_layery = y
                        self.explored_layerx = x
                        

                        test = PointStamped()
                        test.point.x = x
                        test.point.y = y
                        test.header.frame_id = 'map'
                        test.header.stamp = self.test_stamp
                        self.explore_goal.publish(test)
                        #print("X: ",x," Y: ", y)
                        self.goalpose.pose.pose.position.x = x
                        self.goalpose.pose.pose.position.y = y
                        self.goalpose.label = 'explore'
                        self.goalpub.publish(self.goalpose)
                        self.goal_reached = False
                        self.cnt += 1
                else:
                    print("FINISHED EXPLORED")
                    self.speak_bitch("We have finished exploring. viva españa, viva el rey. viva el orden y la ley")
                    self.state = 'goto_object'
                    
            case 'goto_object':
                
                if self.first_iter and self.object_list:

                    goal_object = self.object_list[0]
                    self.goalpose.pose = goal_object[1]
                    self.goalpose.label = 'object'
                    self.goalpub.publish(self.goalpose)
                    # msg = PoseStamped()
                    # msg.pose.position.x = 1.0
                    # msg.pose.position.y = -0.5
                    # q = quaternion_from_euler(0,0,math.pi/2)
                    # msg.pose.orientation.x = q[0]
                    # msg.pose.orientation.y = q[1]
                    # msg.pose.orientation.z = q[2]
                    # msg.pose.orientation.w = q[3]
                    # temp_msg = PointStamped()
                    # temp_msg.header.frame_id = 'map'
                    # temp_msg.header.stamp = self.test_stamp
                    # temp_msg.point.x = self.goalpose.pose.pose.position.x
                    # temp_msg.point.y = self.goalpose.pose.pose.position.y
                    # self.explore_goal.publish(temp_msg)
                    # tempgoal = Information()
                    # tempgoal.pose = msg
                    # tempgoal.label = 'box'
                    # self.goalpub.publish(tempgoal)

                    self.goal_reached = False
                    self.first_iter = False
                    print("GOING TO OBJECT")
                
                elif self.goal_reached:
                    self.first_iter = True
                    self.cnt = 0
                    print("GOING TO Pick")
                    self.state = 'pick'

            case 'goto_box':
                
                if self.first_iter and self.aruco_list:

                    goal_object = self.aruco_list[0]
                    self.goalpose.pose = goal_object[1]
                    self.goalpose.label = 'box'
                    self.goalpub.publish(self.goalpose)
                    # msg = PoseStamped()
                    # msg.pose.position.x = 1.0
                    # msg.pose.position.y = -0.5
                    # q = quaternion_from_euler(0,0,math.pi/2)
                    # msg.pose.orientation.x = q[0]
                    # msg.pose.orientation.y = q[1]
                    # msg.pose.orientation.z = q[2]
                    # msg.pose.orientation.w = q[3]
                    temp_msg = PointStamped()
                    temp_msg.header.frame_id = 'map'
                    temp_msg.header.stamp = self.test_stamp
                    temp_msg.point.x = self.goalpose.pose.pose.position.x
                    temp_msg.point.y = self.goalpose.pose.pose.position.y
                    self.explore_goal.publish(temp_msg)
                    # tempgoal = Information()
                    # tempgoal.pose = msg
                    # tempgoal.label = 'box'
                    # self.goalpub.publish(tempgoal)

                    self.goal_reached = False
                    self.first_iter = False
                    print("GOING TO BOX")
                
                elif self.goal_reached:
                    self.first_iter = True
                    self.cnt = 0
                    print("GOING TO DROP")
                    self.state = 'drop'
                


    
            
            case 'pick':
                max_cnt = 9
                if self.first_iter:
                    self.twist.linear.x = 1.0
                    if abs(self.cnt) < max_cnt:
                        self.twist_pub.publish(self.twist)
                        self.cnt += 1
                    else:
                        self.twist.linear.x = 0.0
                        self.twist_pub.publish(self.twist)
                        self.first_iter = False
                        self.arm_string.data = 'pick'
                        self.arm_pub.publish(self.arm_string)
                        self.cnt = 0
                        for _ in range(50):
                            print("PICK SLEEPING")
                            time.sleep(1)
                        
                else:
                    self.twist.linear.x = -1.0
                    if abs(self.cnt) < max_cnt:
                        self.twist_pub.publish(self.twist)
                        self.cnt += 1
                    else:
                        self.twist.linear.x = 0.0
                        self.twist_pub.publish(self.twist)
                        self.cnt = 0
                        self.first_iter = True
                        self.state = 'goto_box'
            
            case 'drop':
                max_cnt = 9
                if self.first_iter:
                    self.twist.linear.x = 1.0
                    if abs(self.cnt) < max_cnt:
                        self.twist_pub.publish(self.twist)
                        self.cnt += 1
                    else: 
                        self.first_iter = True
                        self.twist.linear.x = 0.0
                        self.twist_pub.publish(self.twist)
                        self.arm_string.data = 'drop'
                        self.arm_pub.publish(self.arm_string)
                        print("DROPING")
                        self.state = ''

            case _:
                if self.first_iter:
                    self.first_iter = False
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
            self.pickup_feedback = msg.data
            self.first_iter = False
            arm_sm_update = Bool()
            arm_sm_update.data = False
            self.arm_feedback_update.publish(arm_sm_update)

    def speak_bitch(self, text):
        time.sleep(2)
        tts = gTTS(text = text, lang = 'es', tld='com.mx')
        filename = "textfile.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    def detected_aurco_callback(self, msg: Information):
        DISTANCE_THRESHOLD = 0.25 #meter
        new_id = msg.label
        new_pose = msg.pose


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
        self.temp_pub.publish(new_pose)
        print("AURCO LIST SIZE: ", len(self.aruco_list))

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
        print("I APPENDED A OBJECT")
        
    def fb_cb(self, pose_msg: Pose):
        self.feedback_obj_pose = pose_msg


def edging(data, res, layery, layerx):
    DIST_THRESHOLD = 50

    min_x = int((layerx+4)/res)
    min_y = int((layery+2)/res)
    #print("MIN_x", min_x, "MIN_y", min_y)
    h, w = data.shape # 1000x700
    # print(h)
    for y in range(min_y, h):
        for x in range(w):
            if data[y][x] != 0:
                pass
            else:
                dist = math.dist([x,y],[min_x, min_y])
                #print("DIST: ", dist)
                if dist < DIST_THRESHOLD:
                    # print("YEEETED DIST")
                    # print("X: ", x, "Y", y)
                    pass
                else:
                    if data[y-1][x] == -1 or data[y+1][x] == -1 or data[y][x+1] == -1 or data[y][x-1] == -1:
                        scaled_y = res*y-2
                        scaled_x = res*x-4
                        return float(scaled_x), float(scaled_y) 
    print("I FUCKED UP")
    
    





    
def main():
    rclpy.init()
    node = StateMachine()
    try:
        rclpy.spin(node, executor=MultiThreadedExecutor(10))
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()