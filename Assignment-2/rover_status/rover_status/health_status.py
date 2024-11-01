
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String

class health_status(Node):

    def __init__(self):
        super().__init__('health_status')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'battery_temp',
            self.listener_callback,
            10)
        self.subscription 
        self.message = ''
        self.publisher_ = self.create_publisher(String, 'rover_health', 10)
        self.timer = self.create_timer(1, self.publish_status)  
        self.get_logger().info("Health status started displaying.")


    def listener_callback(self, msg):
        battery = msg.data[0]
        if battery >= 40:
            self.message= 'Healthy'
        elif battery >= 20:
            self.message = 'Warning'
        else:
            self.message = 'Critical'
    
    def publish_status(self):
        msg1 = String()
        msg1.data = self.message
        self.get_logger().info("Health status sent.")
        self.publisher_.publish(msg1)


def main(args=None):
    rclpy.init(args=args)

    Healh_status = health_status()

    rclpy.spin(Healh_status)
    Healh_status.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
