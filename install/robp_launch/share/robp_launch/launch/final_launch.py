"""Launch phidgets devices in a container."""


import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource


def generate_launch_description():
   phidgets_launch = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('robp_launch'), 'launch'),
         '/phidgets_launch.py'])
      )
   front_camera_launch = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('robp_launch'), 'launch'),
         '/front_camera_launch.py'])
      )
   aruco_launch = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('robp_launch'), 'launch'),
         '/aruco_launch.py'])
      )
   lidar_launch = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('rplidar_ros'), 'launch'),
         '/view_rplidar.launch.py'])
      )
   frames_launch = IncludeLaunchDescription(
      XMLLaunchDescriptionSource([os.path.join(
         get_package_share_directory('robp_launch'), 'launch'),
         '/frames_launch.xml'
      ])
   )


   nodes = [
      ExecuteProcess(
         cmd=['ros2', 'run', 'odometry','odometry'],
         output='screen',
      ),
      ExecuteProcess(
         cmd=['ros2', 'run', 'detection','detection'],
         output='screen',
      ),
      ExecuteProcess(
         cmd=['ros2', 'run', 'display_markers','display_markers'],
         output='screen',
      )
   ]

   return LaunchDescription([
      phidgets_launch,
      front_camera_launch,
      aruco_launch,
      lidar_launch,
      frames_launch,
      *nodes
   ])
