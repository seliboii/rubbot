#!/usr/bin/env python3
import rclpy
import time
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
import rclpy.time
from rubbot_interfaces.action import MoveToGoal
from nav_msgs.msg import OccupancyGrid, Path
from geometry_msgs.msg import PoseStamped, Twist
import numpy as np
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
import math, random
from tf_transformations import quaternion_from_euler, euler_from_quaternion


class MoveToGoalServerNode(Node):
    def __init__(self):
        super().__init__("move_to_goal_server")
        cbg = ReentrantCallbackGroup()
        self.move_to_goal_server_ = ActionServer(
            self, 
            MoveToGoal, 
            "move_to_goal",
            execute_callback=self.execute_callback,
            callback_group=cbg
          )
        
        
        self.get_logger().info("Initializing server...")
        self._og_sub = self.create_subscription(OccupancyGrid,'/occupancy_grid',self.map_callback,1)
        self._path_sub = self.create_subscription(Path, 'path',self.path_callback, 1,callback_group=cbg)
        self.path_pub = self.create_publisher(Path,'/path/goal_path',1)
        self._vel_pub = self.create_publisher(Twist, '/motor_controller/twist',10)



        # self.sample_period = 0.01
        # self.timer = self.create_timer(self.sample_period, self.timer_callback)

        # Global data
        self.iter = 1
        self.start_x = 0
        self.start_y = 0
        self.waypoints = []
        self.width = 0
        self.height = 0
        self.res = 1
        self.data = 0
        self.odom_x = 0
        self.odom_y = 0
        self.odom_theta = 0
        self.atGoal = True
        self.finish_angle = 0
        self.correctAngle = True
        self.get_logger().info("Done bitch")

    
    def map_callback(self, msg:OccupancyGrid):
        self.height = msg.info.height 
        self.width = msg.info.width
        self.res = msg.info.resolution
        self.data = np.reshape(msg.data,(self.height,self.width))

    def path_callback(self, msg: Path):
        latestPose = msg.poses[-1]
        self.odom_x = latestPose.pose.position.x
        self.odom_y = latestPose.pose.position.y
        self.start_x = int((self.odom_x+4)/self.res)
        self.start_y = int((self.odom_y+2)/self.res)
        x = latestPose.pose.orientation.x
        y = latestPose.pose.orientation.y
        z = latestPose.pose.orientation.z
        w = latestPose.pose.orientation.w
        q = euler_from_quaternion([x,y,z,w])
        self.odom_theta = q[2]

    

        if not self.atGoal:
            vel, iter, atGoal = nodeFollow(self.waypoints,self.iter,self.odom_x,self.odom_y,self.odom_theta,self.finish_angle)
            self.iter = iter
            self.atGoal = atGoal
            if vel != 0:
                self._vel_pub.publish(vel)
        
        if not self.correctAngle:
            vel, done = endRotate(self.goal_angle,self.odom_theta)
            if done:
                self.correctAngle = True
            self._vel_pub.publish(vel)
            
            


        

    def execute_callback(self, goal_handle = ServerGoalHandle):
        #Get the request from the goal
        self.iter = 1
        goal_x = int((goal_handle.request.x+4)/self.res)
        goal_y = int((goal_handle.request.y+2)/self.res)
        self.goal_angle = goal_handle.request.angular_z 
        object_type = goal_handle.request.type 
        max_period = goal_handle.request.max_period
        self.get_logger().info("Executing the goal")

        result = MoveToGoal.Result()
        feedback = MoveToGoal.Feedback()
        
        
        path, object_angle, temp = RRT(self,self.height,self.width,self.res,self.data,self.start_x,self.start_y,goal_x,goal_y,object_type)
        self.get_logger().info(str(temp[0]))
        self.get_logger().info(str(temp[1]))
        if object_type == 'object':
            self.goal_angle = object_angle
        if path == False:
            feedback.found_path = False
            goal_handle.publish_feedback(feedback)
            result.reached_goal = False
            goal_handle.abort()
        else:
            goal_handle.succeed()
            feedback.found_path = True
            goal_handle.publish_feedback(feedback)
            goalPath = createPath(self,path)
            self.waypoints = goalPath.poses
            self.atGoal = False
            
            while not self.atGoal:
                time.sleep(0.2)
            
            if object_type != "explore":
                self.correctAngle = False
                while not self.correctAngle:
                    time.sleep(0.2)


            #wait for the at goal to be set to True
                
            result.reached_goal = True
        return result
    
def endRotate(goalTheta, currentTheta):
    done = False
    threshold = math.pi/128
    dutyThreshold = 0.8

    vel = Twist()
    error = goalTheta - currentTheta
    gain = 4

    vel.angular.z = error*gain
    
    if  vel.angular.z > dutyThreshold:
            vel.angular.z = dutyThreshold
    elif vel.angular.z < -dutyThreshold:
        vel.angular.z = -dutyThreshold
    
    
    if abs(error) < threshold:
        done = True
        vel.angular.z = 0.0
    return vel, done
    


def nodeFollow(waypoints,iter,odom_x,odom_y,odom_theta, finish_angle):
    nodeThreshhold = 0.15
    goalThreshhold = 0.08
    done = False
    atGoal = False
    

    if not atGoal:
        x1 = waypoints[iter].pose.position.x
        y1 = waypoints[iter].pose.position.y
        x0 = waypoints[iter-1].pose.position.x
        y0 = waypoints[iter-1].pose.position.y
        

        vel = controller(x1,y1,x0,y0,odom_x, odom_y, odom_theta, done)
        

        distanceToWaypoint = math.dist([waypoints[iter].pose.position.x,waypoints[iter].pose.position.y],[odom_x, odom_y])
        
        if distanceToWaypoint < nodeThreshhold:
            
            if iter != len(waypoints)-1:
                iter += 1
            elif distanceToWaypoint < goalThreshhold:
                done = True
                vel = controller(x1,y1,x0,y0,odom_x, odom_y, odom_theta, done)
                atGoal = True
        return vel, iter, atGoal
    else:
        vel = 0
        return vel, iter, atGoal
    

def controller(gx,gy,x0,y0,odom_x,odom_y,odom_theta,done):
    if not done:
        x = odom_x
        y = odom_y
        theta = odom_theta
        p=0.5
        sample_period = 1/20

        goal_x = gx
        goal_y = gy
        theta_g = math.atan2(goal_y-y0,goal_x-x0)

        d_g = (goal_x-x)*math.cos(theta_g)+(goal_y-y)*math.sin(theta_g)
        d_p = math.sin(theta_g)*(x+p*math.cos(theta)-x0)-math.cos(theta_g)*(y+p*math.sin(theta)-y0)
        L = 0.31
        R = 0.0492

        wGain = 1/(sample_period*R*80)  #40
        vGain = L/(p*sample_period*R*20) #10

        vel = Twist()
        if vGain*d_g > 1.0:
            vel.linear.x = 1.0
        elif vGain*d_g < -1.0:
            vel.linear.x = -1.0
        else:
            vel.linear.x = vGain*d_g
        
        # if abs(theta_g-theta) > math.pi*2/3:
        #     vel.linear.x = 0.0
        #     vel.angular.z = 0.2 #1.0

        if abs(theta_g-theta) > math.pi/16: #/8
            
            vel.linear.x = 0.0
            vel.angular.z = vel.angular.z #*1.5
        
        
        vel.angular.z = wGain*d_p
        #self._vel_pub.publish(vel)
        return vel
    else:
        vel = Twist()
        vel.linear.x = 0.0
        vel.angular.z = 0.0
        return vel

def createPath(self,path):
    goalPath = Path()
    goalPath.header.frame_id = 'map'

    for i in range(len(path)):
        goalPoint = PoseStamped()

        goalPoint.header.frame_id = 'map'
        goalPoint.header.stamp = self.get_clock().now().to_msg()

        goalPoint.pose.position.x = float(path[i][0]*self.res-4)
        goalPoint.pose.position.y = float(path[i][1]*self.res-2)
        goalPoint.pose.position.z = 0.05

        q = quaternion_from_euler(0,0,0)  #path[i][2])
        goalPoint.pose.orientation.x = q[0]
        goalPoint.pose.orientation.y = q[1]
        goalPoint.pose.orientation.z = q[2]
        goalPoint.pose.orientation.w = q[3]
        goalPath.poses.append(goalPoint)
        #print(len(goalPath.poses))
        #goalPath.poses[i] = goalPoint.pose
        
    goalPath.header.stamp = self.get_clock().now().to_msg()
    self.path_pub.publish(goalPath)

    return goalPath
    

class NodePoint():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.theta = 0
        self.phi = 0
        self.parent = None 
        self.cost = 0

def randomNode(h,w,data,nodes,MAX_EDGE_LEN):
    rx = random.randint(0,h-1) #Randomize x and y coordinates
    ry = random.randint(0,w-1)
    distList = []
    for node in nodes:
        distList.append(math.dist([rx,ry],[node.x,node.y])) #Find closest node, might use scipy dist matrix?
    minDist = min(distList)
    parentNode = nodes[distList.index(minDist)] #Get closes node from list
    if minDist > MAX_EDGE_LEN:
        theta = math.atan2(ry-parentNode.y,rx-parentNode.x)
        rx = int(parentNode.x+math.cos(theta)*MAX_EDGE_LEN)
        ry = int(parentNode.y+math.sin(theta)*MAX_EDGE_LEN)
    
    start = [rx,ry]
    end = [parentNode.x,parentNode.y]
    traversed = raytrace(start,end)
    for point in traversed:
        #print("point1: ",point[1],"  point0: ",point[0])
        if data[point[1]][point[0]] == 100: ##HEHEHHEHEHEHEHHEHEHEHEHEH !=0
            return False

    new_node = NodePoint(rx,ry)
    new_node.parent = parentNode
    return new_node
    
def raytrace(start, end): #FLIP START AND END SINCE START SHOULD BE VALID
        """Returns all cells in the grid map that has been traversed
        from start to end, including start and excluding end.
        start = (x, y) grid map index
        end = (x, y) grid map index
        """
        (start_x, start_y) = start
        (end_x, end_y) = end
        x = start_x
        y = start_y
        (dx, dy) = (math.fabs(end_x - start_x), math.fabs(end_y - start_y))
        n = dx + dy
        x_inc = 1
        if end_x <= start_x:
            x_inc = -1
        y_inc = 1
        if end_y <= start_y:
            y_inc = -1
        error = dx - dy
        dx *= 2
        dy *= 2

        traversed = []
        for i in range(0, int(n)):
            traversed.append((int(x), int(y)))

            if error > 0:
                x += x_inc
                error -= dy
            else:
                if error == 0:
                    traversed.append((int(x + x_inc), int(y)))
                y += y_inc
                error += dx

        return traversed    
 
def backTracker(node,path):
    path.append([node.x,node.y])
    node = node.parent
    if node != None:
        backTracker(node,path)
    return path
  
def shortCut(node,goal_node,data):
    start = [goal_node.x,goal_node.y]
    end = [node.x,node.y]
    traversed = raytrace(start,end)
    for point in traversed:
        if data[point[1]][point[0]] != 0: ############HEHEHHEHEHEHHEHEHEHEHEH !=0
            return False
    return True

def bushWacker(node,data):
    if node.parent == None:
        return
    start_node = node
    while shortCut(node.parent,start_node,data):
        node = node.parent
        if node.parent == None:
            break
    start_node.parent = node
    bushWacker(node,data)
    return

def LCHF(node,data):
    daddy = node.parent
    try:
        granddaddy = daddy.parent
    except:
        return
    traversed = raytrace([daddy.x,daddy.y],[node.x,node.y])
    for point in traversed:
        tempNode = NodePoint(point[0],point[1])
        if shortCut(tempNode,granddaddy,data):
            node.parent = tempNode
            tempNode.parent = granddaddy
    
    LCHF(tempNode,data)
    return        

def RRT(self,h,w,res,data,startx,starty,goalx,goaly,object_type):
    max_edge_dist = 15 #Maximum distance between nodes
    max_goal_dist = 5  #Maximum goal distance
    max_object_dist = 30
    iter = 0
    maxIter = 5000 #20000
    angle_2_goal = 0

    goalPath = []
    nodes = []

    if object_type == 'object':
        angle_2_goal = math.atan2(goaly-starty,goalx-startx)
        dist_2_goal = math.dist([starty, startx],[goaly, goalx])
        goalx = startx + math.cos(angle_2_goal)*(dist_2_goal-max_object_dist)
        goaly = starty + math.sin(angle_2_goal)*(dist_2_goal-max_object_dist)

    start_node = NodePoint(startx,starty)
    goal_node = NodePoint(goalx,goaly)
    if shortCut(start_node,goal_node,data) == True:
        goal_node.parent = start_node
        goal_path = backTracker(goal_node,goalPath)
        goal_path.reverse()
        return goal_path, angle_2_goal, [goalx, goaly]


    nodes.append(start_node)
    while iter < maxIter:
        new_node = randomNode(h,w,data,nodes,max_edge_dist)
        if new_node != False:
            nodes.append(new_node)
           
            if shortCut(new_node,goal_node,data) == True:
                
                goal_node.parent = new_node
                bushWacker(new_node,data)
                LCHF(goal_node,data)
                goalPath = backTracker(goal_node,goalPath)
                
                goalPath.reverse()
                return goalPath, angle_2_goal, [goalx, goaly]

        iter += 1
     
        
    return False, angle_2_goal, [goalx, goaly]


def main(args=None):
    rclpy.init(args=args)
    node = MoveToGoalServerNode()
    rclpy.spin(node, executor=MultiThreadedExecutor(3))
    rclpy.shutdown()



if __name__ == "__main__":
    main()