cmake_minimum_required(VERSION 3.8)
project(rover_simulation)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(gazebo_ros REQUIRED)

# Install launch and config files
install(DIRECTORY
  launch
  config
  DESTINATION share/${PROJECT_NAME}/
)

# Install models
install(DIRECTORY
  models
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()

