#!/usr/bin/env python3
from nav2_simple_commander.robot_navigator import BasicNavigator
import rclpy
from copy import deepcopy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose

rclpy.init()
nav = BasicNavigator()
nav.waitUntilNav2Active()
# ======================初始化位置，代替rviz2的2D Pose Estimate===============================
# print("正在initial_pose")
initial_pose = PoseStamped()
initial_pose.header.frame_id = 'map'
initial_pose.header.stamp = nav.get_clock().now().to_msg()
initial_pose.pose.position.x = 0.4
initial_pose.pose.position.y = 0.35
initial_pose.pose.orientation.w = 1.0
# nav.setInitialPose(initial_pose)
# # ...
# print("已经发送初始位置")
#nav.lifecycleStartup()
#nav.waitUntilNav2Active(navigator='bt_navigator', localizer='amcl') # if autostarted, else use lifecycleStartup()
nav.waitUntilNav2Active()
# ...
#test_code
print("正在计算路径")
goal_pose = PoseStamped()
goal_pose.header.frame_id = 'map'
goal_pose.header.stamp = nav.get_clock().now().to_msg()
goal_pose.pose.position.x = 4.65
goal_pose.pose.position.y = 10.0
goal_pose.pose.orientation.w = 1.0


path = nav.getPath(initial_pose, goal_pose)
print(type(path))
smoothed_path = nav.smoothPath(path)
#test_code
print(type(smoothed_path))
#print(type(smoothed_path))
for i in smoothed_path.poses:
    print(i.pose.position.x, i.pose.position.y, i.pose.position.z)
# ...

#nav.goToPose(goal_pose)
# while not nav.isTaskComplete():
#   feedback = nav.getFeedback()
#   if feedback.navigation_duration > 600:
#     nav.cancelTask()

# ...

# result = nav.getResult()
# if result == TaskResult.SUCCEEDED:
#     print('Goal succeeded!')
# elif result == TaskResult.CANCELED:
#     print('Goal was canceled!')
# elif result == TaskResult.FAILED:
#     print('Goal failed!')