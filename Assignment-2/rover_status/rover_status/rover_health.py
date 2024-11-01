
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String


class rover_health(Node):

    def __init__(self):
        super().__init__('rover_health')
        self.subscription1 = self.create_subscription(
            Float32MultiArray,
            'battery_temp',
            self.listener_callback1,
            10)
        self.subscription1 
        self.subscription2 = self.create_subscription(
            String,
            'rover_health',
            self.listener_callback2,
            10)
        self.subscription2

    def listener_callback1(self, msg):
        battery = msg.data[0]
        temp = msg.data[1]
        self.get_logger().info(f'Rover Battery={battery:.2f}%, Rover Temperature={temp:.2f}°C')

    def listener_callback2(self, msg):
        self.get_logger().info(f'Rover Health : {msg.data}')


def main(args=None):
    rclpy.init(args=args)

    Rover_health = rover_health()

    rclpy.spin(Rover_health)
    Rover_health.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
