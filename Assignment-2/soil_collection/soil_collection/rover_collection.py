# rover_navigation/rover_collection.py

import rclpy
from rclpy.node import Node
from mars_msgs.srv import CollectionRequest
import numpy as np
import time

class RoverCollection(Node):
    def __init__(self):
        super().__init__('rover_collection')
        self.srv = self.create_service(CollectionRequest, 'collection_service', self.handle_collection_request)
        
        # Initial rover position and simulated grid with obstacles
        self.position = [0.0, 0.0]
        self.grid_size = (10, 10)
        self.obstacles = self.generate_obstacles()
        self.get_logger().info("Rover collection service is ready.")

    def generate_obstacles(self):
        # Simulate a grid with random obstacles
        grid = np.zeros(self.grid_size)
        obstacle_count = 15
        for _ in range(obstacle_count):
            x, y = np.random.randint(0, self.grid_size[0]), np.random.randint(0, self.grid_size[1])
            grid[x][y] = 1
        return grid

    def handle_collection_request(self, request, response):
        self.get_logger().info(f"Received collection request at ({request.target_x}, {request.target_y})")
        
        # Simulate navigation with obstacle avoidance
        success = self.navigate_to_target(request.target_x, request.target_y)
        
        if success:
            response.success = True
            response.message = f"Sample collection at ({request.target_x}, {request.target_y}) successful."
        else:
            response.success = False
            response.message = f"Sample collection at ({request.target_x}, {request.target_y}) failed due to obstacles."

        self.get_logger().info(response.message)
        return response

    def navigate_to_target(self, target_x, target_y):
        current_x, current_y = self.position
        target = (int(target_x), int(target_y))

        while (int(current_x), int(current_y)) != target:
            # Simulate simple pathfinding with obstacle avoidance
            next_x = current_x + (1 if target_x > current_x else -1 if target_x < current_x else 0)
            next_y = current_y + (1 if target_y > current_y else -1 if target_y < current_y else 0)

            # Check for obstacles
            if self.obstacles[int(next_x)][int(next_y)] == 1:
                self.get_logger().info("Obstacle detected! Adjusting path...")
                return False  # Failed due to obstacle
            else:
                # Update current position
                current_x, current_y = next_x, next_y
                time.sleep(0.5)  # Simulate movement delay
        
        # Update rover position and log success
        self.position = [target_x, target_y]
        return True

def main(args=None):
    rclpy.init(args=args)
    node = RoverCollection()
    rclpy.spin(node)
    rclpy.shutdown()
