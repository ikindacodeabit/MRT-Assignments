import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32MultiArray
from collections import deque
import numpy as np

# Possible moves in 8 directions (row, col)
DIRECTIONS = [
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1),   # right
    (-1, -1), # top-left diagonal
    (-1, 1),  # top-right diagonal
    (1, -1),  # bottom-left diagonal
    (1, 1)    # bottom-right diagonal
]

class RoverNavigation(Node):
    def __init__(self):
        super().__init__('rover_navigation')
        self.navigation_pub = self.create_publisher(String, 'status', 10)
        self.create_subscription(Float32MultiArray, 'obstacle_coordinates', self.receive_obstacles, 10)   
        self.start = (0, 0)  
        self.goal = (8, 9) 

    
    def receive_obstacles(self, msg):
        data = msg.data
        array_2d = np.array(data).reshape(9, 10)
        self.get_logger().info('Received matrix')
        self.get_logger().info(self.rover_navigation(array_2d, self.start, self.goal))

    def is_valid_move(self, matrix, visited, row, col):
        n, m = len(matrix), len(matrix[0])
        return 0 <= row < n and 0 <= col < m and not visited[row][col] and matrix[row][col] == 0

    def rover_navigation(self, matrix, start, goal): 
        self.get_logger().info('Navigating') 
        n, m = len(matrix), len(matrix[0])
        start_row, start_col = self.start
        goal_row, goal_col = self.goal

        if matrix[start_row][start_col] == 1 or matrix[goal_row][goal_col] == 1:
            return "Failure: Start or goal position is an obstacle."

        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[start_row][start_col] = True

        # Queue stores (current position, steps taken)
        queue = deque([(start_row, start_col, 0)])

        while queue:
            row, col, steps = queue.popleft()

            # Check if we have reached the goal
            if (row, col) == (goal_row, goal_col):
                return f"Success: Goal reached in {steps} steps."

            # Explore all 8 possible moves
            for d_row, d_col in DIRECTIONS:
                new_row, new_col = row + d_row, col + d_col

                if self.is_valid_move(matrix, visited, new_row, new_col):
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, steps + 1))

        return "Failure: Path not possible."


def main(args=None):
    rclpy.init(args=args)
    node = RoverNavigation()
    rclpy.spin(node)
    rclpy.shutdown()