import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from mars_msgs.msg import RoverOdometry
from std_msgs.msg import String
import random


class r_data(Node):

    def __init__(self):
        super().__init__('r_data')
        self.rover_id = 101
        self.publisher_ = self.create_publisher(RoverOdometry, 'data', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = RoverOdometry()
        l_vel_x = random.uniform(-4,4)
        l_vel_y = random.uniform(-2,2)
        l_vel_z = random.uniform(-1,1)
        a_vel = random.uniform(-0.0872665,0.0872665) # 0.0872665 rad = 5°
        msg.rover_id = self.rover_id
        msg.orientation = 0.0 # initial orientation set to 0
        msg.linear_velocity.linear.x = l_vel_x
        msg.linear_velocity.linear.y = l_vel_y
        msg.linear_velocity.linear.z = l_vel_z
        msg.angular_velocity = a_vel
        self.publisher_.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    R_data = r_data()
    rclpy.spin(R_data)
    R_data.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()