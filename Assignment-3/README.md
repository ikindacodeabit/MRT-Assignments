# Gazebo Assignment
## How to use:
1) Download the rover simulation folder. 
2) Run the following code in the source of your workspace.
```
colcon build --packages-select rover_simulation
```
3) An example of sending velocity commands to the rover using the ROS2 Topic 'cmd-vel'.
```
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5}, angular: {z: 0.5}}"
```
