#!/usr/bin/env python

import rclpy
from rclpy.node import Node

from robp_interfaces.msg import DutyCycles, Encoders
from geometry_msgs.msg import Twist
from math import pi


class CartesianController(Node):

    def __init__(self):
        super().__init__('cartesian_controller')
        
        # TODO: Implement
        self.dt = 0.1

        self.publisher_dutycycles = self.create_publisher(
            DutyCycles, 
            '/motor/duty_cycles', 
            int(1/self.dt))
        
        self.twist_subscription = self.create_subscription(
            Twist,
            '/motor_controller/twist',
            self.twist_callback,
            int(1/self.dt))
        
        self.encoders_subscription = self.create_subscription(
            Encoders,
            '/motor/encoders',
            self.encoders_callback,
            int(1/self.dt))
        
        self.timer = self.create_timer(self.dt, self.dutycycles_callback)

        self.int_error1 = 0
        self.int_error2 = 0
        self.i = 0 
        self.b = 0.23
        self.r = 0.0352
        self.alpha = 0.1
        self.beta = 0.0 #0.05
        self.dt = 0.1
        self.desired_w1 = 0
        self.desired_w2 = 0
        self.w1 = 0 
        self.w2 = 0
        self.pwm1 = 0
        self.pwm2 = 0        

    # TODO: Implement
        
    def twist_callback(self, msg):
        # self.get_logger().info('I heard: "%s"' % msg)
        w = msg.angular.z
        v = msg.linear.x
        vw1 = (v * 2 - w * 2 * self.b) / 2
        self.desired_w1 = vw1 / (2 * pi * self.r)
        vw2 = (v * 2 + w * 2 * self.b) / 2
        self.desired_w2 = vw2 / (2 * pi * self.r)
        # self.get_logger().info('Twist w1: "%s"' % self.desired_w1)
        # self.get_logger().info('Twist w2: "%s"' % self.desired_w2)
    
    def encoders_callback(self, msg):
        # self.get_logger().info('I heard encoders: "%s"' % msg)
        d2 = msg.delta_encoder_right
        d1 = msg.delta_encoder_left
        self.w1 = d1 / self.dt /360 * 2 * pi
        self.w2 = d2 / self.dt/360 * 2 * pi
        # self.get_logger().info('Encoder w1: "%s"' % self.w1)
        # self.get_logger().info('Encoder w2: "%s"' % self.w2)
        

    def dutycycles_callback(self):

        dsmsg = DutyCycles()
        error1= self.desired_w1 - self.w1
        self.int_error1 += error1 * self.dt
        self.pwm1 = self.alpha * error1 + self.beta * self.int_error1
        
        error2= self.desired_w2 - self.w2
        self.int_error2 += error2 * self.dt
        self.pwm2 = self.alpha * error2 + self.beta * self.int_error2
        
        if self.pwm1 > 1:
            self.pwm1 = 1.0
        elif self.pwm1 < -1:
            self.pwm1 = -1.0
        
        if self.pwm2 > 1:
            self.pwm2 = 1.0
        elif self.pwm2 < -1:
            self.pwm2 = -1.0
        dsmsg.duty_cycle_left = self.pwm1
        dsmsg.duty_cycle_right = self.pwm2
        # dsmsg.duty_cycle_left = 1.0
        # dsmsg.duty_cycle_right = 1.0

        self.publisher_dutycycles.publish(dsmsg)
        self.get_logger().info('Cartesion publishing: "%s"' %dsmsg)
        self.i += 1


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
