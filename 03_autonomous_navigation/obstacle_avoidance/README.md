# Obstacle Avoidance – ROS2

## Overview
Reactive obstacle avoidance using LiDAR data in ROS2.

## Robot
TurtleBot3 (Gazebo simulation)

## Topics Used
- /scan → sensor_msgs/LaserScan
- /cmd_vel → geometry_msgs/Twist

## Logic
- LiDAR divided into left, front, right sectors
- If front < threshold → turn toward free space
- Else → move forward

## Features
- Custom ROS2 Python node
- Launch file support
- Parameter-based threshold
