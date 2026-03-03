import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class AutoMove(Node):

    def __init__(self):
        super().__init__('auto_move_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_turtle)

    def move_turtle(self):
        msg = Twist()
        msg.linear.x = 2.0     # Move forward
        msg.angular.z = 1.0    # Rotate
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing velocity command")

def main(args=None):
    rclpy.init(args=args)
    node = AutoMove()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
