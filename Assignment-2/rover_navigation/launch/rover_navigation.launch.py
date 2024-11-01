from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rover_navigation',
            executable='navigate',
        ),
        Node(
            package='rover_navigation',
            executable='avoid',
        ),
    ])