import rclpy
from rclpy.node import Node
import csv
import numpy as np
from nav_msgs.msg import OccupancyGrid, Path
from map_msgs.msg import OccupancyGridUpdate
from geometry_msgs.msg import PoseStamped
import math
import numpy as np
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
from tf_transformations import quaternion_from_euler, euler_from_quaternion
from tf2_ros.buffer import Buffer
from tf2_ros import TransformException
from tf2_ros.transform_listener import TransformListener
import tf2_geometry_msgs


class Workspace(Node):
    def __init__(self):
        super().__init__('workspace')

        cbg = ReentrantCallbackGroup()
        self.pub = self.create_publisher(OccupancyGrid, '/occupancy_grid', 1)
        self.obstacle_sub = self.create_subscription(PoseStamped, '/object_og', self.detected_object_callback,1,callback_group=cbg)
        self.update_pub = self.create_publisher(OccupancyGridUpdate, 'occupancy_grid_updates',1)
        self._path_sub = self.create_subscription(Path, 'path',self.path_callback, 1,callback_group=cbg)
        self.sample_period = 0.5
        self.timer = self.create_timer(self.sample_period, self.add_obstacle_callback,callback_group=cbg)

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer,self)

        self.start_y = 0
        self.start_x = 0
        self.odom_theta = 0
        self.stamp = 0
        self.ox = 0
        self.oy = 0
        self.otheta = 0
        self.width = 0
        self.obstacle_list = []

        
        with open('/home/g5/dd2419_ws/src/mapping/mapping/workspace.tsv', 'r') as file:

            # read tab seperated file
            reader = csv.reader(file, delimiter='\t')

            # skip the header of the data
            next(reader)

            # define a polygon which will be appended to the data
            polygon = []

            # append data to polygon
            for row in reader:
                polygon.append((float(row[0]), float(row[1])))

        Grid = OccupancyGrid()
        Grid.header.frame_id = 'workspace'
        #Grid.header.stamp = self.get_clock().now().to_msg()

        x_min, x_max = -4, 3
        y_min, y_max = -2, 8
        resolution = 0.01
        self.res = resolution

        # ###################TEMP
        # yaw = -math.pi/2
        # q = quaternion_from_euler(0.0,0.0,yaw)

        # Grid.info.origin.orientation.x = q[0]
        # Grid.info.origin.orientation.y = q[1]
        # Grid.info.origin.orientation.z = q[2]
        # Grid.info.origin.orientation.w = q[3]

        # ############################


        Grid.info.width = int((x_max - x_min) / resolution) 
        Grid.info.height = int((y_max - y_min) / resolution)
        Grid.info.resolution = resolution

        # Grid.info.origin.position.x = float(x_min) #-4
        # Grid.info.origin.position.y = float(y_min) #-2

        x_coordinates = np.linspace(x_min, x_max, Grid.info.width)
        y_coordinates = np.linspace(y_min, y_max, Grid.info.height)

        # X, Y = np.meshgrid(x_coordinates, y_coordinates)

        data = []

        for j, y in enumerate(y_coordinates):
            for i, x in enumerate(x_coordinates):
                if point_inside_polygon(x, y, polygon):
                    data.append(0)
                else:
                    data.append(100)

        Grid.data = data
        self.grid = Grid
    

        #self.pub.publish(Grid)
        print('HERE')

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
        self.stamp = msg.header.stamp

    def detected_object_callback(self, msg: PoseStamped):

        self.obstacle_list.append(msg)
   
      
        


    def add_obstacle_callback(self):
        
        Grid = self.grid
        dataMatrix = np.reshape(Grid.data,(Grid.info.height,Grid.info.width))
        if self.obstacle_list:
            msg = self.obstacle_list[0]
            self.width = msg.pose.position.z/self.res
            to_frame_rel = 'map'
            from_frame_rel = 'camera_link'
            try:
                t = self.tf_buffer.lookup_transform(to_frame_rel,from_frame_rel,msg.header.stamp) #add timeout, around 0.1 sec. Good for the actual project 
                map_pose = tf2_geometry_msgs.do_transform_pose_stamped(msg, t)
                #map_pose = tf2_geometry_msgs.do_transform_pose(msg.pose.pose, t)
                map_pose.pose.position
                self.ox = int((map_pose.pose.position.x+4)/self.res)
                self.oy = int((map_pose.pose.position.y+2)/self.res)
                self.obstacle_list.pop(0)

                if self.ox != 0:

                    dist_2_object = math.dist([self.oy, self.ox],[self.start_y,self.start_x])
                    angle_2_object = math.atan2(self.oy-self.start_y,self.ox-self.start_x)
               
                    
                    
                    right_x = self.start_x + math.cos(angle_2_object)*dist_2_object + math.sin(angle_2_object)*self.width/2
                    right_y = self.start_y - math.cos(angle_2_object)*self.width/2 + math.sin(angle_2_object)*dist_2_object
                    
                    left_x = self.start_x + math.cos(angle_2_object)*dist_2_object - math.sin(angle_2_object)*self.width/2
                    left_y = self.start_y + math.cos(angle_2_object)*self.width/2 + math.sin(angle_2_object)*dist_2_object

                    left_edge = [int(left_x), int(left_y)]
                    right_edge = [int(right_x), int(right_y)]
                    #print(self.width)
                    # print("ROBOT POS: X=", self.start_x," Y=",self.start_y)
                    # print("OBEJCT POS: X=", self.ox," Y=",self.oy)
                    # print("LEFT POS: X=", left_edge[0]," Y=",left_edge[1])
                    # print("RIGHT POS: X=", right_edge[0]," Y=",right_edge[1])

                    ob_traversed = raytrace(left_edge, right_edge)
                    #print(ob_traversed)

                    for ob_point in ob_traversed:
                        try:
                            dataMatrix[ob_point[1]][ob_point[0]] = 100
                        except:
                            return
            
            except TransformException as ex:
                #self.get_logger().info(f'Could not transform {to_frame_rel} to {from_frame_rel}: {ex}')
                #print("NO TRANSFORM")
                pass
                

        

        max_lenght = 150
        camera_span = math.pi/5
        iterations = 200
        for i in range(iterations):
            end_x = int(math.cos(self.odom_theta-camera_span+camera_span*2*i/iterations)*max_lenght+self.start_x)
            end_y = int(math.sin(self.odom_theta-camera_span+camera_span*2*i/iterations)*max_lenght+self.start_y)
            traversed = raytrace([self.start_y, self.start_x],[end_y, end_x])
            unknown = False
            for point in traversed:
                if dataMatrix[point[0]][point[1]] != 100:
                    if unknown:
                        if dataMatrix[point[0]][point[1]] != 0:
                            dataMatrix[point[0]][point[1]] = -1
                    else:
                        dataMatrix[point[0]][point[1]] = 0
                else:
                    unknown = True
        Grid.data = dataMatrix.reshape(-1,).tolist()
        Grid.header.stamp = self.stamp

       
        self.pub.publish(Grid)




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

def point_inside_polygon(x, y, poly):
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y) and y <= max(p1y, p2y) and x <= max(p1x, p2x):
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
            if p1x == p2x or x <= xinters:
                inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def main():
    rclpy.init()
    node = Workspace()
    rclpy.spin(node,executor=MultiThreadedExecutor(3))
    
    # try:
    #     rclpy.spin_once(node,executor=MultiThreadedExecutor(2), timeout_sec=20)
    # except KeyboardInterrupt:
    #     pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()