#!/usr/bin/env python

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16MultiArray, String
from robp_interfaces.msg import ObjPos
from math import sin, cos, acos, asin, atan2, pi

class ARM_IK(Node):

    def __init__(self):
        super().__init__('arm_ik')

        self.obj_sub = self.create_subscription(
            ObjPos,
            '/arm/object', #An object position in form of [activation,x,y]
            self.location_callback, 
            10
        )

        self.pos_publisher = self.create_publisher(
            Int16MultiArray,
            '/arm/arm_pose', #conformation of activation and poses with position for servo 3, 4, 5, 6
            10
        )


        self.obj_pub = self.create_publisher(
            ObjPos,
            '/arm/object', #An object position in form of [activation,x,y]
            10
        )

        self.ik_sta_pub = self.create_publisher(
            String,
            '/arm_state/ik',
            10
        )

        self.timer = self.create_timer(0.1, self.armpos_callback)
        
        self.l1 = 0.101
        self.l2 = 0.094
        self.l3 = 0.169
        self.base_height = 0.16
        self.x_from_base = 0.0
        self.y_from_base = 0.0
        self.x = 0.0
        self.y = 0.0
        self.active = 0.0
        self.box = 0.1
        self.adj = 0.03

    def location_callback(self,msg):
        if msg.activate != 0:
            self.active = msg.activate
            self.x = msg.x
            self.y = msg.y
        else:
            self.active = msg.activate
    
    def armpos_callback(self):
        phi_d = 270.0
        phi = phi_d / 180.0 * pi
        msg = Int16MultiArray()
        obj_msg = ObjPos()
        ik_msg = String()

        if self.active == 1:
            theta6 = atan2(self.y,self.x)
            x1 = (self.x ** 2 + self.y ** 2 ) ** 0.5 - self.l3 * cos(phi) + self.adj
            y1 = - self.base_height - self.l3 * sin(phi)
            c2 = (x1 ** 2 + y1 ** 2 - self.l1 ** 2 - self.l2 ** 2) / (-2 * self.l1 * self.l2)
            xy_distance = (x1 ** 2 + y1 ** 2) ** 0.5 / (self.l1 + self. l2)
            angle_count = 1

            reachability = 1
            print(angle_count)
            
            while abs(xy_distance) > 1:
                if angle_count > 30:
                    print("arm_ik message: postion not reachable")
                    print(x1,y1)
                    ik_msg = String()
                    ik_msg.data = 'fail'
                    self.ik_sta_pub.publish(ik_msg)
                    obj_msg.activate = 0
                    obj_msg.x = 0.0
                    obj_msg.y = 0.0
                    self.obj_pub.publish(obj_msg)
                    reachability = 0
                    break
                phi_d = phi_d + 1.0
                phi = phi_d / 180.0 * pi
                x1 = (self.x ** 2 + self.y ** 2 ) ** 0.5 - self.l3 * cos(phi) + self.adj
                y1 = - self.base_height - self.l3 * sin(phi)
                c2 = (x1 ** 2 + y1 ** 2 - self.l1 ** 2 - self.l2 ** 2) / (-2 * self.l1 * self.l2)
                xy_distance = (x1 ** 2 + y1 ** 2) ** 0.5 / (self.l1 + self. l2)
                angle_count = angle_count + 1
                reachability = 1
                print(angle_count)
                
                
  
                
            if reachability == 1:
                
                rho = acos((self.l2 ** 2 - (x1 ** 2 + y1 ** 2) - self.l1 ** 2)/(-2*self.l1* ((x1 ** 2 + y1 ** 2) ** 0.5)))
                theta5 = atan2(y1,x1) + rho 
                theta4 = acos(c2)
                theta3 = phi - theta5 - theta4
                theta4 = pi - theta4
                theta3 = pi- theta3
                # print("Servo6: ",theta6/pi*180,"Servo5: ",theta5/pi*180,"Servo4: ",theta4/pi*180,"Servo3: ",theta3/pi*180)
                arm_data = [0, int(12000 + theta6/pi*18000), int(12000 - (pi/2 - theta5)/pi*18000), int(12000+theta4/pi*18000), int(12000-theta3/pi*18000)]
                msg.data = arm_data
                self.pos_publisher.publish(msg)
                print("Arm Pose Published: ", msg)
                ik_msg = String()
                ik_msg.data = 'success'
                self.ik_sta_pub.publish(ik_msg)
                obj_msg.activate = 0
                obj_msg.x = 0.0
                obj_msg.y = 0.0
                self.obj_pub.publish(obj_msg)

                
        # elif self.active == 2:
        #     theta6 = atan2(self.y,self.x)
        #     x1 = (self.x ** 2 + self.y ** 2 ) ** 0.5 - self.l3 * cos(phi)
        #     y1 = - self.base_height + self.box - self.l3 * sin(phi)
        #     c2 = (x1 ** 2 + y1 ** 2 - self.l1 ** 2 - self.l2 ** 2) / (-2 * self.l1 * self.l2)
        #     if abs(c2) > 1:
        #         print("arm_ik message: postion not reachable")
        #         ik_msg = String()
        #         ik_msg.data = 'fail'
        #         self.ik_sta_pub.publish(ik_msg)
        #         obj_msg.activate = 0
        #         obj_msg.x = 0.0
        #         obj_msg.y = 0.0
        #         self.obj_pub.publish(obj_msg)
        #     else:
        #         rho = acos((self.l2 ** 2 - (x1 ** 2 + y1 ** 2) - self.l1 ** 2)/(-2*self.l1* ((x1 ** 2 + y1 ** 2) ** 0.5)))
        #         theta5 = atan2(y1,x1) + rho 
        #         theta4 = acos(c2)
        #         theta3 = phi - theta5 - theta4
        #         theta4 = pi - theta4
        #         theta3 = pi- theta3
        #         # print("Servo6: ",theta6/pi*180,"Servo5: ",theta5/pi*180,"Servo4: ",theta4/pi*180,"Servo3: ",theta3/pi*180)
        #         arm_data = [0, int(12000 + theta6/pi*12000), int(theta5/pi*24000), int(12000+theta4/pi*12000), int(12000-theta3/pi*12000)]
        #         msg.data = arm_data
        #         self.pos_publisher.publish(msg)
        #         print("Arm Pose Published: ", msg)
        #         ik_msg = String()
        #         ik_msg.data = 'success'
        #         self.ik_sta_pub.publish(ik_msg)
        #         obj_msg.activate = 0
        #         obj_msg.x = 0.0
        #         obj_msg.y = 0.0
        #         self.obj_pub.publish(obj_msg)
                
        





def main():
    rclpy.init()
    node = ARM_IK()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()