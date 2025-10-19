import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/johanito/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws/install/my_py_pkg'
