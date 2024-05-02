import rclpy
from rclpy.node import Node

from sensor_msgs.msg import PointCloud2, PointField
from sensor_msgs.msg import LaserScan
import sensor_msgs_py.point_cloud2 as pc2
import laser_geometry.laser_geometry as lg
import numpy as np
import random
import tf2_ros
import tf2_py


class Mapping(Node):
    def __init__(self):

        super().__init__('mapping')

        self.lp = lg.LaserProjection()

        self.assoc_map = PointCloud2()
        # self.assoc_map.fields = [   PointField(name='x', offset=0, datatype=7, count=1),
                                    # PointField(name='y', offset=4, datatype=7, count=1),
                                    # PointField(name='z', offset=8, datatype=7, count=1),
                                    # PointField(name='intensity', offset=12, datatype=7, count=1),
                                    # PointField(name='index', offset=16, datatype=5, count=1)]

        self.current_cloud = PointCloud2()
        self.first = True

        # [sensor_msgs.msg.PointField(name='x', offset=0, datatype=7, count=1), 
        # sensor_msgs.msg.PointField(name='y', offset=4, datatype=7, count=1), 
        # sensor_msgs.msg.PointField(name='z', offset=8, datatype=7, count=1), 
        # sensor_msgs.msg.PointField(name='intensity', offset=12, datatype=7, count=1), 
        # sensor_msgs.msg.PointField(name='index', offset=16, datatype=5, count=1)]

        self.init_asoc = PointCloud2()

        self.assoc_map_pub = self.create_publisher(PointCloud2, 'assoc_map', 10)
        self.map_pub = self.create_publisher(PointCloud2, 'current_map', 10)
        self.create_subscription(LaserScan, 'scan', self.scan_cb, 10)

        period = 1
        # updated associate map
        # self.create_timer(period, self.associate_timer)

        # initialized associate map
        
    def associate_timer(self):

        if (self.first):
            self.first = False
            self.assoc_map = self.current_cloud
        else:            
            assoc_points = pc2.read_points(self.assoc_map)
            current_points = pc2.read_points(self.current_cloud)

            aggregate_points = [*assoc_points, *current_points]

            # Probably most efficient to subsample here

            if (len(aggregate_points) > 500):
                random.shuffle(aggregate_points)
                subsample = aggregate_points[:500]
            else:
                subsample = aggregate_points

            # print(len(aggregate_points))
            # print(len(aggregate_points[0]))

            self.assoc_map = pc2.create_cloud(self.current_cloud.header, self.current_cloud.fields, subsample)

            


        self.assoc_map_pub.publish(self.assoc_map)



    def scan_cb(self, msg: LaserScan):
        cloud = self.lp.projectLaser(msg)

        # print(cloud.fields)

        radius2 = (8 * msg.angle_increment) ** 2

        output_cloud = median_filter(cloud, radius2)
        self.current_cloud = output_cloud
        output_cloud.header.stamp = msg.header.stamp

        asoc_points = pc2.read_points(self.init_asoc)
        if (len(asoc_points) < 1000):
            current_points = pc2.read_points(cloud)
            aggregate_points = [*asoc_points, *current_points]

            self.init_asoc = pc2.create_cloud(cloud.header, cloud.fields, aggregate_points)

            self.assoc_map_pub.publish(self.init_asoc)



        # xy = points[:,:2]

        # data = np.frombuffer(cloud.data, dtype=np.float32).reshape(-1, cloud.point_step // 4)
        # xy_data = data[:, :2]

        # filtered_data, width = median_filter(xy, 0.20)

        # cloud.width = width  # Number of points after filtering
        # cloud.is_dense = False  # Indicate that the data may contain invalid points

        # # Define point fields for XY coordinates
        # cloud.fields.append(PointField(name="x", offset=0, datatype=PointField.FLOAT32, count=1))
        # cloud.fields.append(PointField(name="y", offset=4, datatype=PointField.FLOAT32, count=1))
        # cloud.fields.append(PointField(name="z", offset=8, datatype=PointField.FLOAT32, count=1))


        # # Calculate point step and row step
        # cloud.point_step = 12  # 4 bytes for each coordinate (x, y, z)
        # cloud.row_step = cloud.point_step * cloud.width

        # filtered_cloud = pc2.create_cloud(msg.header, fields2d(), filtered_data)

        # cloud.data = filtered_data.astype(np.float32).tobytes()


        self.map_pub.publish(output_cloud)

def rnd_subsample(cloud: PointCloud2) -> PointCloud2:
    gen = pc2.read_points(cloud)
    random.shuffle(gen)

    cloud.data = gen
    return gen

def fields2d():
    fields = [PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
              PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1)]
    return fields
def median_filter(cloud: PointCloud2, radius2:float) -> PointCloud2:

    gen = pc2.read_points(cloud, skip_nans=True)

    output_list = []
    for i, gen_i in enumerate(gen):
        counter = 0
        for j, gen_j in enumerate(gen):
            if (i == j):
                continue
            
            i_dist2 = (gen_i[0]**2 + gen_i[1]**2)

            if distance2([gen_i[0], gen_i[1]], [gen_j[0], gen_j[1]]) < radius2*i_dist2:
                counter += 1

            if counter > 2:
                # output_list.append([coordinate_i[0], coordinate_i[1], 0])
                output_list.append(gen_i)
                break

    
    output_cloud = pc2.create_cloud(cloud.header, cloud.fields, output_list)

    return output_cloud

def distance2(xy1, xy2):

    return (xy1[0] - xy2[0])**2 + (xy1[1] - xy2[1])**2

def main():
    rclpy.init()
    node = Mapping()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()