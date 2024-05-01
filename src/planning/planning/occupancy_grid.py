import rclpy
from rclpy.node import Node

from robp_interfaces.msg import DutyCycles
from nav_msgs.msg import OccupancyGrid
from tf_transformations import quaternion_from_euler
import math

class Occupancy_grid(Node):

    def __init__(self):
        super().__init__('occupancy_grid_pub')
        
        #Create and publish a occupancy grid
        #Later subscribe to localization and object detection to add it to map
        self._ocb_pub = self.create_publisher(OccupancyGrid,'/occupancy_grid',10)


       

        self.og = OccupancyGrid()
        self.og.header.frame_id = 'map'
        self.og.header.stamp = self.get_clock().now().to_msg()

        self.og.info.resolution = 0.01
        self.og.info.height = 300
        self.og.info.width = 300

        self.og.info.origin.position.x = 0.0
        self.og.info.origin.position.y = float(self.og.info.height*self.og.info.resolution/2)
        self.og.info.origin.position.z = 0.0

        yaw = -math.pi/2
        q = quaternion_from_euler(0.0,0.0,yaw)

        self.og.info.origin.orientation.x = q[0]
        self.og.info.origin.orientation.y = q[1]
        self.og.info.origin.orientation.z = q[2]
        self.og.info.origin.orientation.w = q[3]

        # self.og.info.origin.orientation.x = 0.0
        # self.og.info.origin.orientation.y = 0.0
        # self.og.info.origin.orientation.z = 0.0
        # self.og.info.origin.orientation.w = 1.0
        
        data = []
        for i in range(self.og.info.height*self.og.info.width): #left :x right
            if 50 <= i % self.og.info.width <= 90 and 130 <= int(i/self.og.info.width) <= 200:
                data.append(100)
            elif 130 <= i % self.og.info.width <= 180 and 70 <= int(i/self.og.info.width) < 140:
                data.append(100)
            elif 220 <= i % self.og.info.width <= 290 and 140 < int(i/self.og.info.width) < 200:
                data.append(100)
            else:
                data.append(0)
    
        self.og.data = data
        

        timer_period = 1
        self.timer = self.create_timer(timer_period,self.og_publisher)
    
    def og_publisher(self):
        self._ocb_pub.publish(self.og)
    
        
    


def main():
    rclpy.init()
    node = Occupancy_grid()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()


