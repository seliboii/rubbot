#!/usr/bin/env python

import rclpy
import numpy as np
from rclpy.node import Node

from robp_interfaces.msg import DutyCycles, Encoders
from geometry_msgs.msg import Twist


class CartesianController(Node):

    def __init__(self):
        super().__init__('cartesian_controller')
        self.velocity = self.create_subscription(Twist,'/motor_controller/twist',self.velocity_callback,1)
        self.encoder = self.create_subscription(Encoders,'/motor/encoders',self.encoder_callback,10)
        self.duty_cycles_ = self.create_publisher(DutyCycles,'/motor/duty_cycles',10) 
        timer_period = 0.1
        self.timer = self.create_timer(timer_period,self.timer_callback)
        self.i = 0
        self.delta_left = 0
        self.delta_right = 0
        self.linear = 0
        self.angular = 0
        self.int_error_left = 0
        self.int_error_right = 0


    def velocity_callback(self,msg):
        self.linear = msg.linear.x
        self.angular = msg.angular.z
        

    
    def encoder_callback(self,msg):
        #self.left = self.msg.encoder_left
        #self.right = self.msg.encoder_right
        self.delta_left = msg.delta_encoder_left
        self.delta_right = msg.delta_encoder_right

    
    def timer_callback(self):
        #cook the control
        #error = desired_w - estimated_w
        #int_error = int_error + error * dt
        #pwm = alpha * error + beta * int_error
        alpha_left = 0.3 #3
        beta_left = 0.0 #0.05
        alpha_right = 0.3
        beta_right = 0.0 #0.01

        r = 0.0492125
        #r = 0.0352
        base = 0.31
        #base = 0.23 
        tpr = 3200
        freq = 20
        dt = 1/freq
        estimated_left = 2*np.pi*r*freq*self.delta_left/tpr
        desired_left = self.linear-base*self.angular
        left_error = desired_left-estimated_left
        self.int_error_left += left_error*dt
        #self.get_logger().info('error_left: "%s"' % left_error)
        #self.get_logger().info('Int_error_left: "%s"' % self.int_error_left)

        estimated_right = 2*np.pi*r*freq*self.delta_right/tpr
        desired_right = self.linear+base*self.angular
        right_error = desired_right-estimated_right
        self.int_error_right += right_error*dt
        #self.get_logger().info('error_right: "%s"' % right_error)
        #self.get_logger().info('Int_error_right: "%s"' % self.int_error_right)

        pwm_left = alpha_left*left_error+beta_left*self.int_error_left
        pwm_right = alpha_right*right_error+beta_right*self.int_error_right

        msg = DutyCycles()
        if pwm_left > 1.0:
            print("left saturated")
            pwm_left = 1.0
        elif pwm_left < -1.0:
            print("left saturated")
            pwm_left = -1.0

        if pwm_right > 1.0:
            print("right saturated")
            pwm_right = 1.0
        elif pwm_right < -1.0:
            print("right saturated")
            pwm_right = -1.0

        if self.linear == 0 and self.angular == 0:
            pwm_right = 0.0
            pwm_left = 0.0
            
        msg.duty_cycle_left = pwm_left
        msg.duty_cycle_right = pwm_right
        self.duty_cycles_.publish(msg)



        

def main():
    rclpy.init()
    node = CartesianController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()

