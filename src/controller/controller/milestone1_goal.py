import rclpy
from rclpy.node import Node
from robp_interfaces.msg import ObjPos
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Bool
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from tf2_ros import TransformException
import tf2_geometry_msgs
from aruco_msgs.msg import MarkerArray
from geometry_msgs.msg import Twist

import time





class HighLevelController(Node):

    def __init__(self):
        super().__init__('hl_controller')

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.obj_pub = self.create_publisher(
            ObjPos,
            '/arm/object',
            10
        )

        self.goalpos_pub = self.create_publisher(
            PointStamped,
            '/object/position',
            10
        )

        self.arm_done = self.create_subscription(
            Bool,
            '/arm/work_state',
            self.arm_result_cb,
            10
        )

        self.planning_done = self.create_subscription(
            Bool,
            '/planning/status',
            self.plan_result_cb,
            10
        )

        self.planning_trigger_pub = self.create_publisher(
            Bool,
            '/planning/switch',
            10
        )    

        self.velocity = self.create_publisher(Twist,'/motor_controller/twist',10)

        self.aruco = self.create_subscription(MarkerArray,'/marker_publisher/markers',self.aruco_callback,10)

        self.state = 0
        self.state0_result = True
        self.state1_result = True
        self.count = 0


        self.goal_timer = self.create_timer(0.1, self.goal_cb)
        
        self.statemachine = self.create_timer(0.1, self.fsm_cb)

        self.pl_trigger = False

        self.state0_pre = 0

        #self.fsm()

    def fsm_cb(self):

        # state 0, grab object
        if self.state == 0:
            
            self.get_logger().info("Executing state 0")
            # define obj position
            obj_pos = ObjPos()
            obj_pos.activate = 1    # pick command
            obj_pos.x = 0.17    #TODO
            obj_pos.y = 0.0       #TODO

            # publish obj position
            self.obj_pub.publish(obj_pos)
            
            self.state = 1
            self.state0_pre = self.state0_result
                
            # update state
            # self.get_logger().info("Finished state 0")
                
        elif self.state == 1:
            if self.state0_pre != self.state0_result and self.state0_result == False:
                self.state = 2
                self.state0_pre = self.state0_result
            else:
                self.state0_pre = self.state0_result


        # state 1, go to marker
        elif self.state == 2:
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 1.0
            self.velocity.publish(msg)
            # self.state = 2
        # state 2, drop object
        # self.state0_result = True
        elif self.state == 3:
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.velocity.publish(msg)
            self.state = 4
        elif self.state == 4:
            self.get_logger().info("Executing state 1")
            
            # here goal_cb is running to publish goal position
            trigmsg = Bool()
            trigmsg.data = True
            self.planning_trigger_pub.publish(trigmsg)

            # wait until task is done / sleep TODO  
            # while self.state0_result:
            #     print()
            self.get_logger().info(f"{self.state1_result}")
            if self.state1_result == False:
                self.state = 5

        elif self.state == 5:
            trigmsg = Bool()
            trigmsg.data = False
            self.planning_trigger_pub.publish(trigmsg)
            self.count = 0
            self.state = 6
        elif self.state == 6:
            msg = Twist()
            msg.linear.x = 0.3
            msg.angular.z = 0.0
            self.velocity.publish(msg)
            if self.count < 15:
                self.count += 1
            else:
                self.state = 7

        elif self.state == 7:
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.velocity.publish(msg)
            self.state = 8

        elif self.state == 8:
            self.get_logger().info("Executing state 2")

            # drop message
            drop_pos = ObjPos()
            drop_pos.activate = 2    # drop command
            drop_pos.x = 0.14    # TODO
            drop_pos.y = 0.0       # TODO

            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.velocity.publish(msg)

            # publish message
            self.obj_pub.publish(drop_pos)

            self.state = -1

            # wait until task is done / sleep TODO

        elif self.state == -1:
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.velocity.publish(msg)
            self.get_logger().info("FINISH")
            


    def fsm(self):

        i0 = 0        
        while self.state != -1:

            # state 0, grab object
            if self.state == 0:
                
                if i0 == 0:
                    self.get_logger().info("Executing state 0")
                    # define obj position
                    obj_pos = ObjPos()
                    obj_pos.activate = 1    # pick command
                    obj_pos.x = 0.16    #TODO
                    obj_pos.y = 0.0       #TODO

                    # publish obj position
                    self.obj_pub.publish(obj_pos)

                # wait until task is done / sleep TODO    
                    
                # update state
                #self.state = 1
                # self.get_logger().info("Finished state 0")


            # state 1, go to marker
            if self.state == 1:
                self.get_logger().info("Executing state 1")
                
                # here goal_cb is running to publish goal position


                # wait until task is done / sleep TODO  
                # while self.state0_result:
                #     print()

                # update state
                # self.state = 2
                

            # state 2, drop object
            # self.state0_result = True
            if self.state == 2:
                self.get_logger().info("Executing state 2")

                # drop message
                drop_pos = ObjPos()
                obj_pos.activate = 2    # drop command
                obj_pos.x = 0.13    # TODO
                obj_pos.y = 0.0       # TODO

                # publish message
                self.obj_pub.publish(drop_pos)

                # wait until task is done / sleep TODO
                while self.state0_result:
                    print()

    def arm_result_cb(self, msg: Bool):
        self.state0_result = msg.data
        # if self.state0_pre != self.state0_result and self.state0_result == False:
        #     self.state +=1
        #     self.state0_pre = self.state0_result
        # else:
        #     self.state0_pre = self.state0_result

    def plan_result_cb(self, msg: Bool):
        self.state1_result = msg.data

        
    def goal_cb(self):


        if not self.state == 1:
            return
        try:
            t = self.tf_buffer.lookup_transform(
                'aruco/detected1',
                'map',
                rclpy.time.Time(),      #TODO fix timestamping XD
                timeout=rclpy.duration.Duration(seconds=0.05)
            )
        except TransformException as ex:
            # self.get_logger().info(f'could not transform: {ex}')
            return

        p = PointStamped()
        p.header.frame_id = 'map'
        p.header.stamp = t.header.stamp

        p = tf2_geometry_msgs.do_transform_point(p, t)
        self.goalpos_pub.publish(p)

    def aruco_callback(self,msg):
        if self.state == 2:
            self.state = 3

        




def main():
    rclpy.init()
    node = HighLevelController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()