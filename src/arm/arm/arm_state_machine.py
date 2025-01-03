#!/usr/bin/env python

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16MultiArray, String, Bool, Float32MultiArray
from robp_interfaces.msg import ObjPos
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Point


class ARM_SM(Node):

    def __init__(self):
        super().__init__('arm_state_machine')

        self.arm_state_sub = self.create_subscription(
            String,
            '/arm/state_machine',#'active' and 'disable'
            self.arm_state_callback,
            10
        )

        self.arm_state_pub = self.create_publisher(
            String,
            '/arm/state_machine',#'active' and 'disable'
            10
        )

        self.fk_pub = self.create_publisher(
            Float32MultiArray,
            '/arm/forward_kinematic', #conformation of activation and x, y for object relative to center of arm camera image
            10
        )


        self.pos_pub = self.create_publisher(
            Int16MultiArray,
            '/arm/arm_pose', #An pose with position for servo 3, 4, 5, 6, and conformation of activation
            10
        )

        self.obj_pub = self.create_publisher(
            ObjPos,
            '/arm/object', #An object position in form of [activation,x,y]
            10
        )

        self.armcam_sub = self.create_subscription(
            Point,
            '/gripper_position',
            self.armcam_callback,
            10
        )
    
        self.obj_pos_to_statemachine_pub = self.create_publisher(
            Float32MultiArray,
            '/arm_state/obj_pos',
            10
        )

        self.obj_pos_to_statemachine_sub = self.create_subscription(
            Float32MultiArray,
            '/arm_state/obj_pos',
            self.position_recall,
            10
        )

        self.sm_to_ik_pub = self.create_publisher(
            Int16MultiArray,
            '/arm_ik/pos',
            10
        )

        self.ik_sta_pub = self.create_publisher(
            String,
            '/arm_state/ik',
            10
        )

        self.ik_sta_sub = self.create_subscription(
            String,
            '/arm_state/ik', 
            self.ik_sta_callback,
            10
        )

        self.pos_publisher = self.create_publisher(
            Int16MultiArray,
            '/arm/arm_pose', #An pose with position for servo 3, 4, 5, 6, and conformation of activation
            10
        )

        self.pos_sub = self.create_subscription(
            Int16MultiArray,
            '/arm/arm_pose', #An pose with position for servo 3, 4, 5, 6, and conformation of activation
            self.pos_sub_callback,
            10
        )

        self.armstate_sub = self.create_subscription(
            Bool,
            '/arm/work_state',
            self.armstate_callback,
            10
        )

        self.obj_pub = self.create_publisher(
            ObjPos,
            '/arm/object', #An object position in form of [activation,x,y]
            10
        )

        self.arm_pos_sub = self.create_subscription(
            JointState,
            '/servo_pos_publisher', #An pose with position for servo 3, 4, 5, 6, and conformation of activation
            self.cam_pos_callback, 
            10
        )

        self.arm_feedback_update = self.create_publisher(
            Bool,
            '/state_machine/arm',
            10
        )

        self.timer = self.create_timer(0.1, self.state_machine_callback)

    
        self.state = 0

        self.point_count = 0.0
        self.previous_point_x = 0.0
        self.previous_point_y = 0.0
        self.point_stack_x = 0.0
        self.point_stack_y = 0.0
        self.point_ratio = 0.01

        self.obj_x = 0.0
        self.obj_y = 0.0

        self.ik_sta = ' '

        self.pos = [0, 0, 0, 0, 0]

        self.arm_working = False

        self.command = ' '

        self.fb_s1 = 0
        self.fb_s2 = 0
        self.fb_s3 = 0
        self.fb_s4 = 0
        self.fb_s5 = 0
        self.fb_s6 = 0

        self.pick_pose = [12000, 10000, 18000, 2200] # servo 6, servo 5, servo 4, servo 3


    def cam_pos_callback(self,msg):
        self.fb_s1 = msg.position[0]
        self.fb_s2 = msg.position[1]
        self.fb_s3 = msg.position[2]
        self.fb_s4 = msg.position[3]
        self.fb_s5 = msg.position[4]
        #self.fb_s6 = msg.position[5]

    
    def state_machine_callback(self):
        if self.command == 'pick':
            print('pick state: ', self.state)
            if self.state == 0: #set camera to position for detecting object
                arm_pos_msg = Int16MultiArray()
                arm_pos_msg.data = [1, self.pick_pose[0], self.pick_pose[1], self.pick_pose[2], self.pick_pose[3]] # 1 for hold this position
                self.pos_pub.publish(arm_pos_msg)
                self.state = 1
                self.point_count = 0
                self.point_stack_x = 0.0
                self.point_stack_y = 0.0
            elif self.state == 1: #calculate the object position with foward kinematic
                if self.point_count >= 6:
                    armcam_obj_pos = Float32MultiArray()
                    armcam_obj_pos.data = [1.0, self.point_stack_x / (self.point_count - 2.0), self.point_stack_y / (self.point_count - 2.0)]
                    print('Obj Position in Camera: ', armcam_obj_pos.data)
                    self.fk_pub.publish(armcam_obj_pos)
                    self.state = 2
            elif self.state == 2: #publish the object position for inverse kinematic
                if self.obj_x != 0:
                    obj_msg = ObjPos()
                    obj_msg.activate = 1
                    obj_msg.x = self.obj_x
                    obj_msg.y = self.obj_y
                    self.obj_pub.publish(obj_msg)
                    self.obj_x = 0
                    self.obj_y = 0
                    self.state += 1
            elif self.state == 3:
                if self.ik_sta == 'fail':
                    print('cannot pick up')
                    sm_msg = String()
                    sm_msg.data = 'deactive'
                    self.command = 'deactive'
                    self.arm_state_pub.publish(sm_msg)
                    self.reset_arm
                elif self.ik_sta == 'success':
                    pos_msg = Int16MultiArray()
                    pos_msg.data = [2, self.pos[1], self.pos[2], self.pos[3], self.pos[4]]
                    self.pos_pub.publish(pos_msg)
                    self.state += 1
            elif self.state == 4:
                if not self.arm_working:
                    self.reset_arm   
        elif self.command == 'drop':
            print('drop state: ',self.state)
            if self.state == 0:
                arm_pos_msg = Int16MultiArray()
                arm_pos_msg.data = [3, -1, 10000, -1, -1] # 1 for hold this position
                self.pos_pub.publish(arm_pos_msg)
                self.state = 1
            elif self.state == 1:
                if not self.arm_working:
                    self.reset_arm
        else:
            self.reset_arm


    def arm_state_callback(self, msg):
        # print(msg.data)
        if self.command != msg.data:
            self.command = msg.data
            self.state = 0
            arm_sm_update = Bool()
            arm_sm_update.data = True
            self.arm_feedback_update.publish(arm_sm_update)



    def reset_arm(self):
        self.state = 0

        sm_msg = String()
        sm_msg.data = 'deactive'
        self.arm_state_pub.publish(sm_msg)

        fk_msg = Float32MultiArray()
        fk_msg.data = [0.0, 0.0, 0.0]
        self.fk_pub.publish(fk_msg)

        self.obj_x = 0.0
        self.obj_y = 0.0

        print('Arm reset')

        
        


    
    def armcam_callback(self,msg): #get location samples from arm camera and filter them

        # print('Point Count: ', self.point_count)
        # print('Previous Point x: ', self.previous_point_x)
        # print('Msg Point x: ', msg.x)

        if self.point_count == 0.0 and self.previous_point_x != msg.x and self.state == 1:
            if self.pick_pose[1] * 0.9 < self.fb_s5 and self.pick_pose[1] * 1.1 > self.fb_s5:
                if self.pick_pose[2] * 0.9 < self.fb_s4 and self.pick_pose[2] * 1.1 > self.fb_s4:
                    if self.pick_pose[3] * 0.9 < self.fb_s3 and self.pick_pose[3] * 1.1 > self.fb_s3:
                        self.previous_point_x = msg.x
                        self.previous_point_y = msg.y
                        self.point_count += 1.0
                        print('Camera data count: ', self.point_count)
                        self.point_stack_x += msg.x
                        self.point_stack_y += msg.y
            
        elif self.point_count < 6.0 and self.state == 1:
            if self.point_count == 2.0:
                self.point_stack_x = 0
                self.point_stack_y = 0
            if self.previous_point_x != msg.x:
                if self.point_count >= 3:
                    diff = 0.1
                    if abs(msg.x - self.previous_point_x) < 0.03:
                        if abs(msg.y - self.previous_point_y) < 0.03:
                            self.previous_point_x = msg.x
                            self.previous_point_y = msg.y
                            self.point_count += 1.0
                            self.point_stack_x += msg.x
                            self.point_stack_y += msg.y
                            print('Camera data count: ', self.point_count)
                else:
                    self.previous_point_x = msg.x
                    self.previous_point_y = msg.y
                    self.point_count += 1.0
                    self.point_stack_x += msg.x
                    self.point_stack_y += msg.y
                    print('Camera data count: ', self.point_count)



    def armstate_callback(self, msg):
        self.arm_working = msg.data



    def position_recall(self,msg):
        print(msg)
        if msg.data[0] == 1.0:
            self.obj_x = msg.data[1]
            self.obj_y = msg.data[2]
            msg_empty = Float32MultiArray()
            msg_empty.data = [0.0, 0.0, 0.0]
            self.obj_pos_to_statemachine_pub.publish(msg_empty)


    def ik_sta_callback(self, msg):
        if msg.data != ' ':
            self.ik_sta = msg.data
            ik_msg = String()
            ik_msg.data = ' '
            self.ik_sta_pub.publish(ik_msg)


    def pos_sub_callback(self, msg):
        self.pos = msg.data


def main():
    rclpy.init()
    node = ARM_SM()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()