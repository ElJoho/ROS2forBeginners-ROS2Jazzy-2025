# Class 18 — Writing Your First Python Node

## Goal

Create a minimal Python node, run it directly, then install it as a proper ROS2 executable callable with `ros2 run`.

---

## Step 1 — Create the File

Inside the package's inner Python folder (same name as the package):

```bash
cd ~/ros2_ws/src/my_py_pkg/my_py_pkg
touch my_first_node.py
```

Resulting structure:

```
my_py_pkg/
└── my_py_pkg/
    ├── __init__.py
    └── my_first_node.py   ← new file
```

---

## Step 2 — Minimal Node Code

```python
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node = Node("py_test")
    node.get_logger().info("Hello World")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
```

### Anatomy of a ROS2 Python Node

| Line | Purpose |
|---|---|
| `#!/usr/bin/env python3` | Shebang — lets the file run as an executable using Python 3 |
| `import rclpy` | ROS2 Python client library (required in every Python node) |
| `from rclpy.node import Node` | Base `Node` class |
| `rclpy.init(args=args)` | **First line of every ROS2 program** — initializes communications |
| `Node("py_test")` | Creates the node with the name `py_test` |
| `node.get_logger().info(...)` | Prints a log message at INFO level |
| `rclpy.spin(node)` | Keeps the node alive until `Ctrl+C` is pressed |
| `rclpy.shutdown()` | **Last line of every ROS2 program** — clean exit |

> Without `rclpy.spin(node)`, the node would just print and exit immediately. `spin` is a fundamental mechanism in ROS2 — it processes callbacks (topics, services, timers) while the node is alive.

> ⚠️ Always **save the file** (Ctrl+S). VSCode shows a dot on the tab when there are unsaved changes, and a cross when saved.

---

## Step 3 — Run the File Directly (Quick Test)

Make it executable and run it:

```bash
cd ~/ros2_ws/src/my_py_pkg/my_py_pkg
chmod +x my_first_node.py
./my_first_node.py
# [INFO] [1782766829.937156769] [py_test]: Hello World
```

Press `Ctrl+C` to stop. The `KeyboardInterrupt` traceback is normal — it just means `spin` was interrupted as expected.

The log line breaks down as:
```
[INFO]  [timestamp]      [py_test]:  Hello World
 ↑        ↑                 ↑            ↑
 level    time              node name    message
```

---

## Step 4 — Install the Node as an Executable

Running with `./my_first_node.py` works, but the proper ROS2 way is to install the node so it can be launched with `ros2 run` from anywhere (and later from launch files).

Edit `setup.py` and add an entry to `console_scripts`:

```python
entry_points={
    'console_scripts': [
        "py_node = my_py_pkg.my_first_node:main",
    ],
},
```

### Entry Format

```
"<executable_name> = <package>.<file_without_.py>:<function>"
```

| Part | Value in this example |
|---|---|
| Executable name | `py_node` |
| Package | `my_py_pkg` |
| File (no `.py`) | `my_first_node` |
| Function | `main` |

For multiple executables, add comma-separated entries on new lines.

---

## Step 5 — Build and Run with `ros2 run`

Build from the workspace root, then source and run:

```bash
cd ~/ros2_ws
colcon build --packages-select my_py_pkg
# Finished <<< my_py_pkg [1.56s]

source install/setup.bash       # or: source ~/.bashrc
ros2 run my_py_pkg py_node
# [INFO] [1782767329.142999799] [py_test]: Hello World
```

> Whenever you add or install something new in the workspace, re-source it (or open a new terminal if `.bashrc` already sources the workspace).

> Tab autocompletion works on both the package name and the executable name — if it doesn't autocomplete, something is wrong with the install or sourcing.

---

## ⚠️ Three Different Names — Don't Confuse Them

This is a common source of confusion:

| Name | Where it's defined | Example here |
|---|---|---|
| **File name** | The `.py` filename | `my_first_node.py` |
| **Node name** | Inside the code: `Node("...")` | `py_test` |
| **Executable name** | In `setup.py` console_scripts | `py_node` |

They can be identical (e.g. a `temperature_sensor.py` file with a `temperature_sensor` node and a `temperature_sensor` executable), but they are conceptually **three separate things**. Different names were used here on purpose to make this clear.

---

## Summary of the Workflow

```
1. touch my_first_node.py         ← create file
2. write the code                  ← init → Node → spin → shutdown
3. chmod +x + ./file.py            ← quick test (optional)
4. edit setup.py console_scripts   ← register executable
5. colcon build --packages-select  ← build from ~/ros2_ws
6. source install/setup.bash       ← refresh environment
7. ros2 run my_py_pkg py_node      ← run anywhere
```

---

## What's Next

- Rewrite the node using **object-oriented programming** (subclass `Node`) — this becomes the reusable template for all future nodes.