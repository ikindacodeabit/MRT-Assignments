# rover_navigation/collection_client.py

import rclpy
from rclpy.node import Node
from mars_msgs.srv import CollectionRequest

class CollectionClient(Node):
    def __init__(self):
        super().__init__('collection_client')
        self.client = self.create_client(CollectionRequest, 'collection_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("Collection service not available, waiting...")

    def send_request(self, target_x, target_y):
        request = CollectionRequest.Request()
        request.target_x = target_x
        request.target_y = target_y

        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            self.get_logger().info(f"Response: {future.result().message}")
        else:
            self.get_logger().error("Service call failed.")

def main(args=None):
    rclpy.init(args=args)
    client = CollectionClient()

    # Example list of target coordinates
    target_coordinates = [(2, 3), (5, 5), (9, 9)]

    for target_x, target_y in target_coordinates:
        client.get_logger().info(f"Requesting collection at ({target_x}, {target_y})")
        client.send_request(float(target_x), float(target_y))

    rclpy.shutdown()
