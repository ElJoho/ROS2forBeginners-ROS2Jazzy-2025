# Class 16 — Creating a ROS2 C++ Package

## Command to Create the Package

Run this from inside your workspace's `src/` folder:

```bash
cd ~/ros2_ws/src
ros2 pkg create my_cpp_pkg --build-type ament_cmake --dependencies rclcpp
```

| Option | Value | Purpose |
|---|---|---|
| `--build-type` | `ament_cmake` | Marks this as a C++ package |
| `--dependencies` | `rclcpp` | C++ client library for ROS2 |

> Compare with Python: `--build-type ament_python` and `--dependencies rclpy`

The `[WARNING]` about the license is harmless — just means no LICENSE file was generated. Ignore it for now.

---

## Package Structure Generated

```
my_cpp_pkg/
├── include/
│   └── my_cpp_pkg/      ← header files (.hpp / .h)
├── src/                  ← implementation files (.cpp)
├── CMakeLists.txt        ← build rules
└── package.xml           ← package metadata & dependencies
```

This is a standard C++ project layout wrapped in a ROS2 package.

- `src/` → `.cpp` implementation files (nodes go here)
- `include/my_cpp_pkg/` → `.hpp` / `.h` header files
- `CMakeLists.txt` → defines how to compile the package (revisited when writing the first node)
- `package.xml` → the one mandatory file in every ROS2 package; lists name, version, build type (`ament_cmake`), and dependencies (`<depend>rclcpp</depend>`)

---

## Building

Always build from the **workspace root**, not from `src/`:

```bash
cd ~/ros2_ws
colcon build
```

Build a single package (faster during development):

```bash
colcon build --packages-select my_cpp_pkg
```

> ⚠️ If you accidentally run `colcon build` inside `src/`, delete the generated folders before continuing:
> ```bash
> rm -rf build install log
> ```
> Then re-run `colcon build` from the workspace root.

---

## package.xml — Key Fields

```xml
<name>my_cpp_pkg</name>
<version>0.0.0</version>
<build_type>ament_cmake</build_type>
<depend>rclcpp</depend>
```

To add more dependencies later, append more `<depend>` tags below the existing one.

---

## What's Next

- Create the first C++ node inside `src/`
- Write the corresponding build rules in `CMakeLists.txt`
- Run and inspect nodes with command-line tools