# 02 – Turtlesim Projects (ROS2 Fundamentals)

This module contains foundational ROS2 experiments using the Turtlesim simulator.

Turtlesim was used to understand:
- ROS2 Nodes
- Topics (Publisher/Subscriber)
- Message types
- Services
- Timers
- Basic motion control logic

---

##  Learning Objectives

- Create custom ROS2 Python packages
- Publish velocity commands to `/turtle1/cmd_vel`
- Subscribe to `/turtle1/pose`
- Use services like `/spawn` and `/kill`
- Implement basic autonomous motion

---

##  Projects Included

### 🔹 1. Basic Turtle Movement
**Concepts:**
- geometry_msgs/Twist
- rclpy publisher

**Command to run:**
```bash
ros2 run <package_name> turtle_move_node
