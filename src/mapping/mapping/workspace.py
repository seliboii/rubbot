import rclpy
from rclpy.node import Node
import csv
import numpy as np
from nav_msgs.msg import OccupancyGrid

class Workspace(Node):
    def __init__(self):
        super().__init__('workspace')

        self.pub = self.create_publisher(OccupancyGrid, 'grid/workspace', 1)
        
        with open('/home/rosuser/rubbot/src/mapping/mapping/workspace.tsv', 'r') as file:

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
        Grid.header.frame_id = 'map'

        x_min, x_max = -4, 3
        y_min, y_max = -2, 8
        resolution = 0.01


        Grid.info.width = int((x_max - x_min) / resolution) + 1
        Grid.info.height = int((y_max - y_min) / resolution) + 1
        Grid.info.resolution = resolution

        Grid.info.origin.position.x = float(x_min)
        Grid.info.origin.position.y = float(y_min)

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

        self.pub.publish(Grid)
        print('HERE')



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
    try:
        rclpy.spin_once(node, timeout_sec=1)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()