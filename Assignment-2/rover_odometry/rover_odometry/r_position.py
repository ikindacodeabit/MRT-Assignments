
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String
from mars_msgs.msg import RoverOdometry


class r_position(Node):
    def __init__(self):
        super().__init__('r_position')
        self.subscription = self.create_subscription(
            RoverOdometry,
            'data',
            self.listener_callback,
            10)
        self.subscription 
        self.x = 0
        self.y = 0
        self.z = 0
        self.angle = 0
        self.orientation = 0
        self.get_logger().info('Started recieving data')



    def listener_callback(self, msg):
        self.x += msg.linear_velocity.linear.x * 1
        self.y += msg.linear_velocity.linear.y * 1
        self.z += msg.linear_velocity.linear.z * 1
        self.angle += msg.angular_velocity * 1
        if msg.linear_velocity.linear.x >= 3:
            self.get_logger().info(f'Warning! Speed exceeds 3 m/s')
        self.get_logger().info(f'X={self.x:.2f}, Y={self.y:.2f}, Z={self.z:.2f}, angle = {self.angle:.2f}')


        

def main(args=None):
    rclpy.init(args=args)
    R_position = r_position()
    rclpy.spin(R_position)
    R_position.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
