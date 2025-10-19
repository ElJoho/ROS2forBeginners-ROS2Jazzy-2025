johanito@johanito-HP-Pavilion-11-x360-PC:~/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws/src$ ros2 pkg create my_cpp_pkg --build-type ament_cmake --dependencies rclcpp
going to create a new package
package name: my_cpp_pkg
destination directory: /home/johanito/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['johanito <johalopezari@unal.edu.co>']
licenses: ['TODO: License declaration']
build type: ament_cmake
dependencies: ['rclcpp']
creating folder ./my_cpp_pkg
creating ./my_cpp_pkg/package.xml
creating source and include folder
creating folder ./my_cpp_pkg/src
creating folder ./my_cpp_pkg/include/my_cpp_pkg
creating ./my_cpp_pkg/CMakeLists.txt

[WARNING]: Unknown license 'TODO: License declaration'.  This has been set in the package.xml, but no LICENSE file has been created.
It is recommended to use one of the ament license identifiers:
Apache-2.0
BSL-1.0
BSD-2.0
BSD-2-Clause
BSD-3-Clause
GPL-3.0-only
LGPL-3.0-only
MIT
MIT-0
johanito@johanito-HP-Pavilion-11-x360-PC:~/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws/src$ ls
my_cpp_pkg  my_py_pkg
johanito@johanito-HP-Pavilion-11-x360-PC:~/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws/src$ cd ..
johanito@johanito-HP-Pavilion-11-x360-PC:~/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws$ colcon build
Starting >>> my_cpp_pkg
Starting >>> my_py_pkg  