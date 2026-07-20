cmake_minimum_required(VERSION 3.0.2)
project(week2_ros_practice)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/target_pub.py
  scripts/target_sub.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
