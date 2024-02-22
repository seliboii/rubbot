
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(#ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0 -v6
            package='micro_ros_agent',
            executable='micro_ros_agent',
            arguments=  ['serial', '--dev', '/dev/ttyUSB0', '-v6']
        ),
        Node(#ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0 -v6
            package='arm',
            namespace = 'arm',
            executable='arm_ik',
            name = 'InverseKinematic',
            output='screen'
        ),
        Node(#ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0 -v6
            package='arm',
            namespace = 'arm',
            executable='arm_control',
            name = 'ArmController'
        )
    ])