#!/usr/bin/env python



import rclpy

from rclpy.node import Node



from robp_interfaces.msg import DutyCycles, Encoders

from geometry_msgs.msg import Twist





class CartesianController(Node):



    def __init__(self):

        super().__init__('cartesian_controller')



        self.cum_error_left = 0

        self.cum_error_right = 0

        self.vel = 0

        self.ang_vel = 0

        self.right_speed = 0

        self.left_speed = 0



        self.freq = 20

        self.tpr = 3200

        self.radius = 0.0492125

        self.dt = 1 / self.freq

        self.base = 0.31


        self.encoderSubscriber = self.create_subscription(

            Encoders,

            '/motor/encoders',

            self.encoder_cb,

            10

        )

        self.encoderSubscriber



        self.twistSubscriber = self.create_subscription(

            Twist,

            '/motor_controller/twist',

            self.twist_cb,

            10

        )

        self.twistSubscriber



        self.dutycyclePublisher = self.create_publisher(

            DutyCycles,

            '/motor/duty_cycles',

            10

        )

        timer_period = 0.05  #seconds

        self.timer = self.create_timer(timer_period, self.timer_callback)

    

    def timer_callback(self):

        msg = DutyCycles()

        prop_gain = 1




        desired_left_w = self.vel - self.base*self.ang_vel

        desired_right_w = self.vel + self.base*self.ang_vel



        # Calculating error in left wheel and computing control

        estimated_left_w = self.left_speed



        error_left = desired_left_w - estimated_left_w

        self.cum_error_left = self.cum_error_left + error_left * self.dt

        pwm_left = prop_gain * error_left + 3 * self.cum_error_left



        # Calculating error in right wheel and computing control

        estimated_right_w = self.right_speed



        error_right = desired_right_w - estimated_right_w

        self.cum_error_right = self.cum_error_right + error_right * self.dt

        pwm_right = prop_gain * error_right + 3 * self.cum_error_right



        msg.duty_cycle_left = constrain(pwm_left)

        msg.duty_cycle_right = constrain(pwm_right)



        #msg.duty_cycle_left = 1.0

        #msg.duty_cycle_right = 1.0

        self.dutycyclePublisher.publish(msg)

        self.get_logger().info('Pwm left: %s' %pwm_left)

        self.get_logger().info('Pwm right: %s' % pwm_right)





    def encoder_cb(self, msg):

        self.left_speed = (2*3.141592 * self.radius * self.freq * msg.delta_encoder_left)/self.tpr

        self.right_speed = (2*3.141592 * self.radius * self.freq * msg.delta_encoder_right)/self.tpr



        self.get_logger().info('encoder callback')



        x = (self.left_speed + self.right_speed)/2

        w = (self.left_speed - self.right_speed) / (2*self.base)



        self.get_logger().info('Linear velocity: %s' % x)

        self.get_logger().info('Angular velocity: %s' % w)



    def twist_cb(self, msg):    

        self.vel = msg.linear.x

        self.ang_vel = msg.angular.z

        #self.get_logger().info('twist callback')





def constrain(pwm):

    if pwm > 1:

        return 1.0

    if pwm < -1:

        return -1.0

    return pwm

    

def rad2tick(rad):

    return (180/3.141592) * rad 



def tick2rad(tick):

    return (3.141592/180) * tick



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