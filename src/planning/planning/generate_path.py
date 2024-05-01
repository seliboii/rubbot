import rclpy
import random
import math
from rclpy.node import Node
import numpy as np
from robp_interfaces.msg import DutyCycles
from nav_msgs.msg import OccupancyGrid, Path
from geometry_msgs.msg import PoseStamped, PointStamped
from tf_transformations import quaternion_from_euler
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
import tf2_geometry_msgs


class Generate_Path(Node):

    def __init__(self):
        super().__init__('path_pub')

        self._og_sub = self.create_subscription(OccupancyGrid,'/occupancy_grid',self.map_callback,1)
        self._get_goal = self.create_subscription(PoseStamped, '/move_base_simple/goal',self.goal_callback,10)
        self.path_pub = self.create_publisher(Path,'/path/goal_path',10)
        self._path_sub = self.create_subscription(Path, 'path',self.path_callback, 10)

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)


        self.start_x = 0
        self.start_y = 0

        self.width = 0
        self.height = 0
        self.res = 1
        self.data = 0
        self.origin_X = 0
        self.origin_Y = 0
        # self.tree = []
        
    def path_callback(self, msg: Path):
        latestPose = msg.poses[-1]
        self.start_x = int((latestPose.pose.position.x+4)/self.res)
        self.start_y = int((latestPose.pose.position.y+2)/self.res)
   


    def map_callback(self, msg: OccupancyGrid):
        self.height = msg.info.height 
        self.width = msg.info.width
        self.res = msg.info.resolution
        # self.origin_X = msg.info.origin.x
        # self.origin_Y = msg.info.origin.y
        self.data = np.reshape(msg.data,(self.height,self.width))

        
    
       
        
        
        
        

    
    def goal_callback(self,msg: PoseStamped):
        goal_x = int((msg.pose.position.x+4)/self.res)   
        goal_y = int((msg.pose.position.y+2)/self.res) 

        
        path = RRT(self,self.height,self.width,self.res,self.data,self.start_x,self.start_y,goal_x,goal_y)
    
        if path == False:
            print("Couldnt find cock")
        else:
            publishPath(self,path,cock=True)
        


def publishPath(self,path,cock):
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
    if cock == True:
        self.path_pub.publish(goalPath)
    if cock == False:
        self.branch_pub.publish(goalPath)

    return
    

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
        if data[point[1]][point[0]] != 0:
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

# def backTracker(node,path):
#     traversed = raytrace([node.x,node.y],[node.parent.x,node.parent.y])
#     path.extend(traversed)
#     node = node.parent
#     if node.parent != None:
#         backTracker(node,path)
#     return path
   


def shortCut(node,goal_node,data):
    start = [goal_node.x,goal_node.y]
    end = [node.x,node.y]
    traversed = raytrace(start,end)
    for point in traversed:
        if data[point[1]][point[0]] != 0:
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
        

    


def RRT(self,h,w,res,data,startx,starty,goalx,goaly):
    print("Looking for path")
    max_edge_dist = 15 #Maximum distance between nodes
    max_goal_dist = 5  #Maximum goal distance
    iter = 0
    maxIter = 50000

    goalPath = []
    nodes = []


    start_node = NodePoint(startx,starty)
    goal_node = NodePoint(goalx,goaly)
    if shortCut(start_node,goal_node,data) == True:
        #goalPath = raytrace([start_node.x,start_node.y],[goal_node.x,goal_node.y])
        #goalPath.reverse()
        print("Found a direct path!")
        goal_node.parent = start_node
        goal_path = backTracker(goal_node,goalPath)
        goal_path.reverse()
        print(len(goal_path))
        return goal_path


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

                print(len(goalPath))
                print("Found a path!")
                return goalPath

        iter += 1

    print("Could not find a Path")
    return False



    

    


def main():
    rclpy.init()
    node = Generate_Path()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()