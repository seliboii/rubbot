import rclpy
from rclpy.node import Node
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
    try :
        rclpy.spin(node)
    except KeyboardInterrupt :
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()
