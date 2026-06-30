# Class 19 — Python Node with OOP + Timer

## Why OOP?

- **Official ROS2 recommendation** — all ROS2 example code uses it
- **Scalable** — adding subscribers, publishers, timers, etc. stays clean
- Becomes a **reusable template** for every future node you write

---

## Final Code

```python
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("Hello World")
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
```

This ~20-line structure is the **template for every Python node** going forward. Change the class name and the node name string, and the skeleton stays the same.

---

## Anatomy

### Class definition

```python
class MyNode(Node):
```

`MyNode` **inherits from `Node`** → it gets all ROS2 node functionality (loggers, timers, publishers, subscribers, etc.) accessible via `self.`.

> For a temperature sensor: `class TemperatureSensorNode(Node):` — name the class after what the node does.

### Constructor

```python
def __init__(self):
    super().__init__("py_test")   # parent constructor — sets the node name
```

`super().__init__("py_test")` calls the `Node` parent constructor, which is what actually registers the node with ROS2 and gives it the name `py_test`.

### Logger inside the class

```python
self.get_logger().info("Hello World")
```

Same as before, but now `self.` instead of `node.` — because the class **is** the node.

### Simplified main

```python
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()      # ← just instantiate the class
    rclpy.spin(node)
    rclpy.shutdown()
```

The main is unchanged in pattern: **init → create node → spin → shutdown**. Only the node creation line changed.

---

## Timers — One of the Most Important ROS2 Features

A timer calls a function repeatedly at a fixed interval as long as the node is spinning. Used for any periodic task (read a sensor at 10 Hz, publish at 1 Hz, etc.).

### Creating a Timer

```python
self.create_timer(1.0, self.timer_callback)
```

| Parameter | Meaning |
|---|---|
| `1.0` | Period in seconds (float) — here, fire every 1 second |
| `self.timer_callback` | The function to call **(no parentheses!)** |

### ⚠️ No parentheses on the callback

```python
self.create_timer(1.0, self.timer_callback)    # ✅ pass reference
self.create_timer(1.0, self.timer_callback())  # ❌ calls it immediately
```

Without parentheses you pass the **reference**; the timer calls it later (hence: *callback*).

### How it Works with `spin`

```
main → rclpy.spin(node)   ← blocks here, processes callbacks
              ↓
         every 1 second
              ↓
     timer_callback() fires
```

`spin` is what allows the timer (and later, subscribers and services) to actually run their callbacks. No spin → no callbacks.

---

## Convention: Trailing Underscore for Class Attributes

```python
self.counter_ = 0    # trailing underscore = class attribute convention
```

This is a convention the instructor uses to distinguish class attributes from local variables. Be consistent — the terminal log below shows what happens if you mix `self.counter` and `self.counter_`.

---

## Workflow (unchanged): Build → Source → Run

```bash
cd ~/ros2_ws
colcon build --packages-select my_py_pkg
# Finished <<< my_py_pkg [1.54s]

. install/setup.bash       # shorthand for: source install/setup.bash
ros2 run my_py_pkg py_node
```

Expected output:

```
[INFO] [...] [py_test]: Hello World
[INFO] [...] [py_test]: Hello 0
[INFO] [...] [py_test]: Hello 1
[INFO] [...] [py_test]: Hello 2
...
```

`Hello World` prints once (from the constructor), then `Hello N` prints every second (from the timer callback).

---

## 🐛 Build Errors vs Runtime Errors — A Real Example

This is an important Python/ROS2 distinction the instructor warns about.

### Syntax errors → caught at build time

```
File ".../my_first_node.py", line 15
    self.counter += + 1
SyntaxError: invalid syntax
```
→ `colcon build` **fails**, you see the error immediately.

### Logic / attribute errors → caught only at runtime

From the actual terminal:

```
AttributeError: 'MyNode' object has no attribute 'counter'.
Did you mean: 'counter_'?
```

What happened: `self.counter_` was defined in `__init__`, but the callback used `self.counter` (no underscore). Python is dynamically typed → **the build succeeded**, the error only appeared the second the timer fired.

**Lesson:** a successful `colcon build` on a Python package does **not** mean the code is bug-free. Run the node and watch the logs.

---

## Template Summary

The reusable skeleton (strip the timer/counter if not needed):

```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("node_name")
        # publishers, subscribers, timers, etc. go here

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
```

---

## What's Next

- Same node logic, but written in **C++** using `rclcpp`
- More ROS2 communication primitives (publishers, subscribers, services) — all attached to the node class the same way as the timer