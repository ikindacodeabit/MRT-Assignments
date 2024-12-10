from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
import os

def generate_launch_description():
    # Get the path to the model.sdf file
    package_name = 'rover_simulation'
    model_path = os.path.join(
        os.path.expanduser('~'),
        'ros2_ws/install', 
        package_name, 
        'share', 
        package_name, 
        'models/rover/model.sdf'
    )

    # Launch Gazebo
    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )

    # Spawn the rover model
    spawn_rover = Node(
        package='gazebo_ros', 
        executable='spawn_entity.py', 
    arguments=[
        '-entity', 'rover',  
        '-file', model_path,  
        '-x', '1.0',  # Start 1m to the right of the origin
        '-y', '2.0',  # Start 2m forward from the origin
        '-z', '0.5'   # Start 0.5m above the ground
    ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_rover
    ])
