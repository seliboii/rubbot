
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(#ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0 -v6
            package='micro_ros_agent',
            executable='micro_ros_agent',
            arguments=  ['serial', '--dev', '/dev/ttyUSB0', '-v6']
        ),
        Node(#ros2 run arm arm_ik
            package='arm',
            namespace = 'arm',
            executable='arm_ik',
            name = 'InverseKinematic',
            output='screen'
        ),
        Node(#ros2 run arm arm_control
            package='arm',
            namespace = 'arm',
            executable='arm_control',
            name = 'ArmController'
        ),
        Node(#ros2 run arm arm_fk
            package='arm',
            namespace = 'arm',
            executable='arm_fk',
            name = 'ArmFowardKinematic'
        )
        # ,
        # Node(#ros2 run arm arm_control
        #     package='arm',
        #     namespace = 'arm',
        #     executable='arm_state_machine',
        #     name = 'ArmStateMachine'
        # )
        # ,
        # Node(
        #     package='usb_cam',
        #     executable='usb_cam_node'
        # ),
        # Node(
        #     package='ros2pkg',
        #     executable='ros2pkg',
        #     arguments=['exec', '--prefix', 'usb_cam', 'ros2', 'launch', 'usb_cam', 'camera.launch.py']
        # ),
        # Node(
        #     package='image_proc',
        #     executable='image_proc',
        #     name='image_proc',
        #     arguments=['--ros-args', '--remap', '/image:=/camera1/image_raw', '--remap', '/camera_info:=/camera1/camera_info']
        # )
    ])
