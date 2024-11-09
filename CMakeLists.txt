cmake_minimum_required(VERSION 3.0.2)
project(pluto_camera_stream)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS src/stream_camera.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
