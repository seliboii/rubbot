import rclpy
from rclpy.node import Node

from robp_interfaces.msg import DutyCycles
from nav_msgs.msg import Path
from tf_transformations import quaternion_from_euler, euler_from_quaternion
from geometry_msgs.msg import Twist
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from geometry_msgs.msg import PoseStamped


import math

class Path_Follower(Node):

    def __init__(self):
        super().__init__('path_follower')
        self._path_sub = self.create_subscription(Path, 'path',self.path_callback, 1)


        self._path_sub = self.create_subscription(Path, '/path/goal_path',self.goalpath_callback,1)

        
        self._vel_pub = self.create_publisher(Twist, '/motor_controller/twist',10)
    
        self.sample_period = 0.01
        self.timer = self.create_timer(self.sample_period, self.timer_callback)

        
        self.iter = 1
        self.waypoints = []
        self.endpoint = 0
        self.odom_x = 0
        self.odom_y = 0
        self.odom_theta = 0


    def goalpath_callback(self, msg: Path):
        self.iter = 1
        self.waypoints = msg.poses
        #self.endpoint = [msg.poses[-1].pose.position.x,msg.poses[-1].pose.position.y]
        #print(len(self.waypoints))

    def path_callback(self, msg: Path):
        latestPose = msg.poses[-1]
        self.odom_x = latestPose.pose.position.x
        self.odom_y = latestPose.pose.position.y
        x = latestPose.pose.orientation.x
        y = latestPose.pose.orientation.y
        z = latestPose.pose.orientation.z
        w = latestPose.pose.orientation.w
        q = euler_from_quaternion([x,y,z,w])
        self.odom_theta = q[2]
        


        
        
    
    def timer_callback(self):
        nodeThreshhold = 0.15
        goalThreshhold = 0.10
        done = False
        

        if self.waypoints:
            x1 = self.waypoints[self.iter].pose.position.x
            y1 = self.waypoints[self.iter].pose.position.y
            x0 = self.waypoints[self.iter-1].pose.position.x
            y0 = self.waypoints[self.iter-1].pose.position.y
    
            controller(self,x1,y1,x0,y0,done)

            distanceToWaypoint = math.dist([self.waypoints[self.iter].pose.position.x,self.waypoints[self.iter].pose.position.y],[self.odom_x, self.odom_y])
            if distanceToWaypoint < nodeThreshhold:
                if self.iter != len(self.waypoints)-1:
                    self.iter += 1
                elif distanceToWaypoint < goalThreshhold:
                    done = True
                    controller(self,x1,y1,x0,y0,done)
                    self.waypoints.clear()
                    print("AT THE GOAL POSITION")












        
            


def controller(self,gx,gy,x0,y0,done):
    if not done:
        x = self.odom_x
        y = self.odom_y
        theta = self.odom_theta
        p=0.3

        goal_x = gx
        goal_y = gy
        theta_g = math.atan2(goal_y-y0,goal_x-x0)

        


        d_g = (goal_x-x)*math.cos(theta_g)+(goal_y-y)*math.sin(theta_g)
        d_p = math.sin(theta_g)*(x+p*math.cos(theta)-x0)-math.cos(theta_g)*(y+p*math.sin(theta)-y0)
        L = 0.31
        R = 0.0492

        wGain = 1/(self.sample_period*R*300)
        vGain = L/(p*self.sample_period*R*100)
        
        


        vel = Twist()
        # print("vGAIN times d_g: ",vGain*d_g)
        # print("wGAIN times d_p: ",wGain*d_p)
        if vGain*d_g > 1.0:
            vel.linear.x = 1.0
        elif vGain*d_g < -1.0:
            vel.linear.x = -1.0
        else:
            vel.linear.x = vGain*d_g
        
        if abs(theta_g-theta) > math.pi/8:
            print(theta_g)
            
            vel.linear.x = 0.0
        
        vel.angular.z = wGain*d_p
        self._vel_pub.publish(vel)
        return
    else:
        vel = Twist()
        vel.linear.x = 0.0
        vel.angular.z = 0.0
        self._vel_pub.publish(vel)




def main():
    rclpy.init()
    node = Path_Follower()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()


