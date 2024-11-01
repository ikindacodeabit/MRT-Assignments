from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='soil_collection',
            executable='service',
        ),
        Node(
            package='soil_collection',
            executable='client',
        ),

    ])