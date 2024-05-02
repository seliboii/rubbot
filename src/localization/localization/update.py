import rclpy
import rclpy.duration
from rclpy.node import Node
<<<<<<< HEAD
from scipy.spatial import KDTree, transform
import rclpy.time
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import PoseStamped, TransformStamped
import sensor_msgs_py.point_cloud2 as pc2
from tf2_ros import TransformBroadcaster, TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup


from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster


import tf2_geometry_msgs
import numpy as np
from scipy.optimize import least_squares
from scipy.spatial import procrustes

def icp(mapp: PointCloud2, source: PointCloud2, pose_estimate: PoseStamped, max_iterations = 50):
    map_array = pc2.read_points(mapp, skip_nans=True, field_names=('x', 'y'))
    reference_array = pc2.read_points(source, skip_nans=True, field_names=('x', 'y'))
    bob = []
    for things in map_array:
        x, y = things
        bob.append([x,y])
    cob = []
    for things in reference_array:
        x, y = things
        cob.append([x,y])

    map_array = np.array(bob)
    ref_array = np.array(cob)


    xy_map = map_array[:,:2]  
    xy_ref = ref_array[:,:2]

    theta = pose_estimate.pose.orientation.z
    tx = pose_estimate.pose.position.x
    ty = pose_estimate.pose.position.y

    R = np.array(  [[np.cos(theta), -np.sin(theta)], 
                    [np.sin(theta),  np.cos(theta)]])
    t = np.array([[tx], 
                  [ty]])

    tree = KDTree(xy_ref, copy_data=True)
    for iteration in range(max_iterations):
        
        # rotate and translate map
        tf_map = ((R@xy_map.T) + t).T
        distances, indices = tree.query(tf_map)
        associations = xy_ref[indices]

        # find minimizing rotation and translation
        R, t = find_rotation_translation(tf_map, associations)

    #print("Rotation matrix: ", len(R), " translation: ", len(t))   
    return R, t
        
def find_rotation_translation(A, B):
    # Step 2: Center the data
    A = A.T
    B = B.T
    centroid_A = np.mean(A, axis=1)
    centroid_B = np.mean(B, axis=1)
    centered_A = A - centroid_A[:, np.newaxis]
    centered_B = B - centroid_B[:, np.newaxis]

    # Step 3: Compute the covariance matrix
    H = centered_A @ centered_B.T

    # Step 4: Perform SVD
    U, _, Vt = np.linalg.svd(H)

    # Step 5: Compute Rotation and Translation
    R = np.dot(Vt, U)
    t_r = R @ centroid_A
    t = np.array([centroid_B - t_r]).T

    return R, t

def r2theta(R) -> float:
    theta1 = np.arccos(R[0][0])
    theta2 = np.arcsin(R[1][0])

    if theta2 > 0:
        return theta1
    else:
        return -theta1



            
def opt_fun(pose, M, S):

    tx = pose[0]
    ty = pose[1]
    theta = pose[2]

    tf = np.array([ [np.cos(theta), -np.sin(theta), tx],
                    [np.sin(theta),  np.cos(theta), ty],
                    [0, 0, 1]])
    S = np.transpose(S)

    Mmmm = (tf@M.T).T[:,:2]

    bing = Mmmm - S
    objective = np.linalg.norm(bing[:,0] - bing[:,1])

    return objective

        

class Update(Node):

    def __init__(self):
        super().__init__('update')

        cbg = ReentrantCallbackGroup()

        self.map = PointCloud2()
        self.cmap = PointCloud2()


        # Initialize the transform listerner and assign it a buffer
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.create_subscription(PointCloud2, 'assoc_map', self.ass_cb, 10, callback_group=cbg)
        self.create_subscription(PointCloud2, 'current_map', self.cmap_cb, 10)
        self._tf_broadcaster = TransformBroadcaster(self)


        self.ready = False

        self.transf = TransformStamped()
        self.transf.child_frame_id = 'odom'
        self.transf.header.frame_id = 'map'

        self.transf.header.stamp = self.map.header.stamp
        # failed = True
        # from_frame_rel = 'base_link'
        # to_frame_rel = 'odom'
        # while failed:
        #     try:
        #         tmp = self.tf_buffer.lookup_transform(to_frame_rel, from_frame_rel, time=rclpy.time.Time(), timeout=rclpy.duration.Duration(seconds=1.0))
        #     except TransformException as ex:
        #         self.get_logger().info(
        #                 f'Could not transform {from_frame_rel} to {to_frame_rel}: {ex}')
        #     else:
        #         print('Success')
        #         print(tmp.header.stamp)
        #         break
        # self.tf_static_broadcaster = StaticTransformBroadcaster(self)
        # self.tf_static_broadcaster.sendTransform(self.transf)

        self.create_timer(1.0, self.timer_cb)

    def ass_cb(self, msg: PointCloud2):
        self.map = msg
        print(msg.header.stamp)


    def cmap_cb(self, msg: PointCloud2):
        self.cmap = msg

    def timer_cb(self):
        if self.ready:
            try:
                map2base = self.tf_buffer.lookup_transform('base_link','map', rclpy.time.Time()) #add timeout, around 0.1 sec. Good for the actual project 

            except TransformException as ex:
                self.get_logger().info(
                            f'Could not transform map to base_link: {ex}')
                return 
            # Initial guess, should be from odometry
            pose = tf2_geometry_msgs.do_transform_pose_stamped(PoseStamped(), map2base)
            R, t = icp(self.cmap, self.map, pose)

            theta = r2theta(R)
            self.transf.transform.rotation.z = theta
            print("Theta: ", (theta*180)/np.pi)
            print("tx, ty: ", t[0][0], t[1][0])
            self.transf.transform.translation.x = t[0][0]
            self.transf.transform.translation.y = t[1][0]
            self.transf.header.stamp = self.cmap.header.stamp

            self._tf_broadcaster.sendTransform(self.transf)
        else:
            # try:
                # tmp = self.tf_buffer.lookup_transform('odom', 'map', rclpy.time.Time())
            # except TransformException as ex:
                # self.get_logger().info(
                            # f'Could not transform map to base_link: {ex}')
                # return
            self.transf.header.stamp = self.map.header.stamp
            self._tf_broadcaster.sendTransform(self.transf)
            if self.map.header.stamp.nanosec.bit_length() > 0:
                self.ready = True
                
            
        

def main() :
    rclpy.init()
    node = Update()
    executor = MultiThreadedExecutor(2)
=======
from rclpy.duration import Duration

from tf2_ros.transform_listener import TransformListener
from tf2_ros import TransformBroadcaster
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from geometry_msgs.msg import TransformStamped, PoseStamped, Transform
from tf2_geometry_msgs import do_transform_pose_stamped

class update(Node):

    def __init__(self) :
        super().__init__('update')

        # Initialize the transform listerner and assign it a buffer
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer,self)

        # Initialize the transform broadcaster
        self._tf_broadcaster = TransformBroadcaster(self)

        self.create_subscription(PoseStamped, 'localization/landmark_measured', self.update_cb, 10)
        # static transform

    # Compute map to odom transform from a landmark constraint
    def update_cb(self, msg: PoseStamped):
        t1 = self.tf_buffer.lookup_transform('landmark', 'map')
        try:
            t2 = self.tf_buffer.lookup_transform('odom', 
                                                 msg.header.frame_id, 
                                                 msg.header.stamp,
                                                 Duration(seconds=0.1))
        except TransformException as ex:
            self.get_logger().info(f'{ex}')
            return

        m2b_pose = do_transform_pose_stamped(msg, t1)
        m2o = do_transform_pose_stamped(m2b_pose, t2)

        m2o_transform = TransformStamped()
        m2o_transform.header.frame_id = 'map'
        m2o_transform.child_frame_id = 'odom'
        m2o_transform.transform.rotation = m2o.pose.orientation
        m2o_transform.transform.translation = m2o.pose.position

        self._tf_broadcaster.sendTransform(m2o_transform)

    

def main() :
    rclpy.init()
    node = update()
>>>>>>> 7b94ee2a65c6ea62d38ee0dc4109a5bf6eb4f318
    try :
        rclpy.spin(node, executor)
    except KeyboardInterrupt :
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()
