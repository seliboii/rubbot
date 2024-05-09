#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from robp_interfaces.msg import Information
import math
from tf_transformations import euler_from_quaternion, quaternion_from_euler


class StateMachine(Node):
    def __init__(self):
        super().__init__('test_statemachine')

        sm_period = 0.1
        self.state = 'init'
        self.create_timer(sm_period, self.sm_cb)
        self.count = 0
        self.entry = True

        # publishers
        self.twist_pub = self.create_publisher(
            Twist,
            '/motor_controller/twist',
            1
        )

        # subscribers
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

        # initialize
        self.twist_msg = Twist()
        self.object_list = []
        self.aruco_list = []



    def sm_cb(self):
        match self.state:
            case 'init':
                self.get_logger().info('In init state')
                self.state = 'rotate'

            case 'rotate':
                if self.count % 5 == 0:
                    self.get_logger().info('Rotating...')
                if self.count < 40:
                    self.twist_msg.angular.z = 1.2566
                else:
                    self.twist_msg.angular.z = 0.0
                    self.state = 'check_for_pickup'
                    self.get_logger().info('checking for pickup')
                
                self.twist_pub.publish(self.twist_msg)
                self.count += 1
            
            case 'check_for_pickup':
                if not self.object_list:    # check if empty
                    self.get_logger().info("object list is empty, going to explore")
                    self.state = 'explore'
                else:                       # if not empty
                    self.get_logger().info("object list is not empty, time for pickup task")
                    self.state = 'go2object'

            # TODO
            case 'explore':
                if not self.object_list:    # check if empty, then keep exploring
                    None
                else:                       # if not empty, go to pickup task
                    self.state = 'check_for_pickup'
                self.state = 'TODO'

            # TODO
            case 'go2object':
                self.state = 'pick'
            
            # TODO
            case 'pick':
                self.object_inhand = self.object_list[0][0]
                self.state = 'check_for_dropoff'
            
            case 'check_for_dropoff':
                if not self.aruco_list:     # check if empty
                    self.get_logger().info('aruco list is empty, going to explore')
                    self.state = 'explore'
                else:
                    boxid = obj2box(self.object_inhand)
                    foundbox = False
                    for markers in self.aruco_list:
                        if boxid == markers[0]:
                            foundbox = True

                    if foundbox:
                        self.get_logger().info('matched ID for object in hand and detected aruco marker')
                        self.state = 'go2box'
                    else:
                        self.get_logger().info('No matching aruco marker in list, going to explore')
                        self.state = 'explore'

            case _:
                self.get_logger().info('In default state state')

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

def obj2box(object: str)->int:
    box_id = 0
    match object:
        case 'cube':
            box_id = 1
        case 'ball':
            box_id = 2
        case 'animal':
            box_id = 3
        case _:
            box_id = -1
            print('WHAT, line 106 in sm_ms3.py')
    return box_id

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