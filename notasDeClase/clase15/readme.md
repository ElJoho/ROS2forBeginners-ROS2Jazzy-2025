johanito@johanito-HP-Pavilion-11-x360-PC:~/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws/src$ ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy 
going to create a new package
package name: my_py_pkg
destination directory: /home/johanito/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['johanito <johalopezari@unal.edu.co>']
licenses: ['TODO: License declaration']
build type: ament_python
dependencies: ['rclpy']
creating folder ./my_py_pkg
creating ./my_py_pkg/package.xml
creating source folder
creating folder ./my_py_pkg/my_py_pkg
creating ./my_py_pkg/setup.py
creating ./my_py_pkg/setup.cfg
creating folder ./my_py_pkg/resource
creating ./my_py_pkg/resource/my_py_pkg
creating ./my_py_pkg/my_py_pkg/__init__.py
creating folder ./my_py_pkg/test
creating ./my_py_pkg/test/test_copyright.py
creating ./my_py_pkg/test/test_flake8.py
creating ./my_py_pkg/test/test_pep257.py

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
my_py_pkg
johanito@johanito-HP-Pavilion-11-x360-PC:~/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws/src$ cd ..
johanito@johanito-HP-Pavilion-11-x360-PC:~/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws$ colcon build
Starting >>> my_py_pkg
Finished <<< my_py_pkg [15.9s]            

Summary: 1 package finished [16.9s]
johanito@johanito-HP-Pavilion-11-x360-PC:~/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws$ colcon build --packages-select my_py_pkg
Starting >>> my_py_pkg
Finished <<< my_py_pkg [7.14s]          

Summary: 1 package finished [8.07s]
