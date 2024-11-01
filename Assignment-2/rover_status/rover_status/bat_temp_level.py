
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import random

class BatteryTempPublisher(Node):
    def __init__(self):
        super().__init__('battery_temp_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'battery_temp', 10)
        self.timer = self.create_timer(1, self.publish_status)  
        self.get_logger().info("Battery and Temperature Publisher started.")

    def publish_status(self):
        msg = Float32MultiArray()
        battery_level = random.uniform(0, 100)  
        temperature = random.uniform(-20, 80)  
        msg.data = [battery_level, temperature]

        #self.get_logger().info(f'Publishing: Battery={battery_level:.2f}%, Temp={temperature:.2f}°C')
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = BatteryTempPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
