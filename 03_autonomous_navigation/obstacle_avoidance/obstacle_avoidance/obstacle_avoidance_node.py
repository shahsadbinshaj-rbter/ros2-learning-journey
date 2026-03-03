import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np


class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance_node')

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)

        self.threshold = 0.5  # meters
        self.get_logger().info("Obstacle Avoidance Node Started")

    def scan_callback(self, msg):
        ranges = np.array(msg.ranges)

        # Replace inf values with large number
        ranges = np.nan_to_num(ranges, nan=10.0, posinf=10.0, neginf=10.0)

        # Sector division (TurtleBot3 LiDAR is 360 degrees)
        left = np.min(ranges[60:120])
        front = np.min(ranges[0:30].tolist() + ranges[330:360].tolist())
        right = np.min(ranges[240:300])

        cmd = Twist()

        if front < self.threshold:
            self.get_logger().info("Obstacle detected! Turning...")
            if left > right:
                cmd.angular.z = 0.5
            else:
                cmd.angular.z = -0.5
        else:
            cmd.linear.x = 0.2

        self.publisher.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
