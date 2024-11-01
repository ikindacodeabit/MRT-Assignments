import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, String
import numpy as np
import argparse

class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance')
        self.obstacle_pub = self.create_publisher(Float32MultiArray, 'obstacle_coordinates', 10)
        #self.create_subscription(String, 'status', self.update_obstacle_reference, 10) 
        self.rover_position = (0, 0)  
        self.rows = 0
        self.columns = 0
        self.publish_obstacles()

        
    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Input matrix dimensions and elements.')
        parser.add_argument('m', type=int, help='Number of rows in the matrix')
        parser.add_argument('n', type=int, help='Number of columns in the matrix')
        parser.add_argument('elements', nargs='+', type=float, help='Matrix elements in row-major order')
        args = parser.parse_args()
        self.rows = args.m
        self.columns = args.n
        # Check if the number of elements matches m * n
        if len(args.elements) != args.m * args.n:
            raise ValueError(f'Expected {args.m * args.n} elements, but got {len(args.elements)}')
        
        # Reshape elements into m x n matrix
        matrix = np.array(args.elements).reshape(args.m, args.n)
        return matrix

    def publish_obstacles(self):
        route =  self.parse_arguments()
        msg = Float32MultiArray()
        msg.data = np.array(route, dtype=np.float32).flatten().tolist()
        self.get_logger().info('Publishing matrix')
        self.obstacle_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    rclpy.spin(node)
    rclpy.shutdown()