#!/usr/bin/env python

import rclpy
from rclpy.node import Node

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from tf2_ros import TransformBroadcaster
import tf2_geometry_msgs

from aruco_msgs.msg import MarkerArray
from geometry_msgs.msg import TransformStamped


class DisplayMarkers(Node):

    def __init__(self) :
        super().__init__('display_markers')

    
        # Initialize the transform listerner and assign it a buffer
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer,self)
        

        # Initialize the transform broadcaster
        
        self._tf_broadcaster = TransformBroadcaster(self)


        # Subscribe to aruco marker topic and call callback function on each recieved message
        self.aruco = self.create_subscription(MarkerArray,'/marker_publisher/markers',self.aruco_callback,10)

        


    def aruco_callback(self, msg: MarkerArray):
            arucoFrame = msg.header.frame_id
            try:
                t = self.tf_buffer.lookup_transform('map',arucoFrame,msg.markers[0].header.stamp) #add timeout, around 0.1 sec. Good for the actual project 
                self.get_logger().info("kuken")

            except:
                #self.get_logger().info("kuken")
                return
            map_pose = tf2_geometry_msgs.do_transform_pose(msg.markers[0].pose.pose, t)
            t.transform.translation.x = map_pose.position.x
            t.transform.translation.y = map_pose.position.y
            t.transform.translation.z = map_pose.position.z
            t.transform.rotation.x = map_pose.orientation.x
            t.transform.rotation.y = map_pose.orientation.y
            t.transform.rotation.z = map_pose.orientation.z
            t.transform.rotation.w = map_pose.orientation.w
            id = msg.markers[0].id
            t.header.frame_id = 'map'
            t.header.stamp = msg.markers[0].header.stamp
            t.child_frame_id = '/aruco/detected'+str(id)
            self._tf_broadcaster.sendTransform(t)
            
         

        # look up transform from map_frame to marker frame and publish the position of each marker
        # Broadcast/publish the transform between the map frame and the detected aruco marker

def main() :
    rclpy.init()
    node = DisplayMarkers()
    try :
        rclpy.spin(node)
    except KeyboardInterrupt :
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()



""" std_msgs/Header header
	builtin_interfaces/Time stamp
		int32 sec
		uint32 nanosec
	string frame_id
aruco_msgs/Marker[] markers
	std_msgs/Header header
		builtin_interfaces/Time stamp
			int32 sec
			uint32 nanosec
		string frame_id
	uint32 id
	geometry_msgs/PoseWithCovariance pose
		Pose pose
			Point position
				float64 x
				float64 y
				float64 z
			Quaternion orientation
				float64 x 0
				float64 y 0
				float64 z 0
				float64 w 1
		float64[36] covariance
	float64 confidence """