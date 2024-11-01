from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rover_status',
            executable='bat_temp',
        ),
        Node(
            package='rover_status',
            executable='status',
        ),
        Node(
            package='rover_status',
            executable='r_status',
        )
    ])