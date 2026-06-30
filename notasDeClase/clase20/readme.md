# Class 20 — Writing Your First C++ Node

## Goal

Same node concept as in Python, now in C++. Workflow: write `.cpp` → declare the executable in `CMakeLists.txt` → build → source → run.

> Unlike Python, C++ is compiled — you **cannot** test the file directly with `./file`. It must be built first.

---

## Step 1 — Create the File

C++ source files go in the package's `src/` folder:

```bash
cd ~/ros2_ws/src/my_cpp_pkg/src
touch my_first_node.cpp
```

Resulting structure:

```
my_cpp_pkg/
├── include/my_cpp_pkg/
├── src/
│   └── my_first_node.cpp   ← new file
├── CMakeLists.txt
└── package.xml
```

---

## Step 2 — Minimal Node Code

```cpp
#include "rclcpp/rclcpp.hpp"

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<rclcpp::Node>("cpp_test");
    RCLCPP_INFO(node->get_logger(), "Hello world");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
```

### Anatomy

| Line | Purpose |
|---|---|
| `#include "rclcpp/rclcpp.hpp"` | C++ ROS2 client library (required in every C++ node) |
| `rclcpp::init(argc, argv);` | **First line** — initializes ROS2 communications |
| `auto node = std::make_shared<rclcpp::Node>("cpp_test");` | Creates a **shared pointer** to a `Node` named `cpp_test` |
| `RCLCPP_INFO(node->get_logger(), "Hello world");` | Logs at INFO level (macro, not a method) |
| `rclcpp::spin(node);` | Keeps the node alive until `Ctrl+C` |
| `rclcpp::shutdown();` | **Last line** — clean exit |
| `return 0;` | Standard `int main` return |

> 💡 Save the file right after writing the `#include`. Autocompletion for `rclcpp::` only works reliably after VSCode picks up the saved include.

---

## Pointers in ROS2 C++

ROS2 uses **smart pointers everywhere** — specifically `std::shared_ptr`.

```cpp
auto node = std::make_shared<rclcpp::Node>("cpp_test");
//   ↑                ↑                  ↑
//   shared_ptr<Node> factory function   constructor argument
```

- `std::make_shared<T>(...)` allocates a `T` and returns a `shared_ptr<T>` to it
- Memory is managed automatically — no `new` / `delete`
- Since `node` is a pointer, use `->` (not `.`) to access members:

```cpp
node->get_logger()    // ✅ access object through pointer
node.get_logger()     // ❌ would access the shared_ptr itself
```

> Worth a quick brush-up on smart pointers if they're new to you — but in practice the pattern is always `auto x = std::make_shared<SomeRosClass>(...)` and then `x->method()`.

---

## Step 3 — Declare the Executable in `CMakeLists.txt`

Open `my_cpp_pkg/CMakeLists.txt`. After cleaning up the unused `BUILD_TESTING` block, the relevant additions are between `find_package` and `ament_package()`:

```cmake
cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

# create the executable
add_executable(cpp_node src/my_first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)

# install the executable
install(TARGETS
  cpp_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
```

### The Three Important Blocks

**1. `add_executable`** — declares the executable and its source file:
```cmake
add_executable(cpp_node src/my_first_node.cpp)
#              ↑          ↑
#       executable name   path to .cpp from package root
```

**2. `ament_target_dependencies`** — links libraries to the executable:
```cmake
ament_target_dependencies(cpp_node rclcpp)
#                         ↑       ↑
#                  executable   libraries (space-separated)
```
> Forgetting this → compile error: *"rclcpp not found"*.

**3. `install(TARGETS ...)`** — installs the binary so `ros2 run` can find it:
```cmake
install(TARGETS
  cpp_node
  DESTINATION lib/${PROJECT_NAME}
)
```
> ⚠️ Common typo: `${PROJECT_NAME}` — must be **dollar sign + curly braces + PROJECT_NAME exactly**. Any typo silently breaks the install.

### Adding More Executables Later

Only the `add_executable` + `ament_target_dependencies` lines need to be duplicated per executable. The `install(TARGETS ...)` block can list multiple executable names:

```cmake
install(TARGETS
  cpp_node
  another_node
  yet_another_node
  DESTINATION lib/${PROJECT_NAME}
)
```

### For Every New Dependency

If you later use another ROS2 package (e.g. `std_msgs`):
```cmake
find_package(std_msgs REQUIRED)
ament_target_dependencies(cpp_node rclcpp std_msgs)
```
And add `<depend>std_msgs</depend>` to `package.xml`.

---

## Step 4 — Build, Source, Run

Always from the workspace root:

```bash
cd ~/ros2_ws
colcon build --packages-select my_cpp_pkg
# Finished <<< my_cpp_pkg [3.18s]

. install/setup.bash
ros2 run my_cpp_pkg cpp_node
# [INFO] [1782831589.285068710] [cpp_test]: Hello world
```

`Ctrl+C` to stop — C++ shutdown is cleaner than Python's:

```
^C[INFO] [...] [rclcpp]: signal_handler(SIGINT/SIGTERM)
```
(no Python-style traceback)

---

## 🐛 Build Errors — More Strict Than Python

C++ catches **way more** at build time than Python does. Example from the lesson — forgetting the node name argument:

```cpp
auto node = std::make_shared<rclcpp::Node>();   // ❌ missing "cpp_test"
```

→ `colcon build` fails with a wall of template/compiler errors. Look for:

```
Failed   <<< my_cpp_pkg
```

vs the success line:

```
Finished <<< my_cpp_pkg
```

That `Failed` / `Finished` distinction is how you confirm whether the build worked.

> Trade-off vs Python: more errors at compile time = fewer runtime surprises. The `AttributeError`-at-runtime situation from the Python version is much less likely in C++.

---

## ⚠️ Three Different Names (Same Lesson as Python)

| Name | Where defined | Example here |
|---|---|---|
| **File name** | The `.cpp` filename | `my_first_node.cpp` |
| **Node name** | Inside the code: `rclcpp::Node("...")` | `cpp_test` |
| **Executable name** | In `CMakeLists.txt` → `add_executable(...)` | `cpp_node` |

`ros2 run` uses the **executable name**. The logs show the **node name**. Three distinct things.

---

## Python vs C++ Side-by-Side

| Step | Python | C++ |
|---|---|---|
| Library | `rclpy` | `rclcpp` |
| Init | `rclpy.init(args=args)` | `rclcpp::init(argc, argv);` |
| Create node | `node = Node("name")` | `auto node = std::make_shared<rclcpp::Node>("name");` |
| Log | `node.get_logger().info("msg")` | `RCLCPP_INFO(node->get_logger(), "msg");` |
| Spin | `rclpy.spin(node)` | `rclcpp::spin(node);` |
| Shutdown | `rclpy.shutdown()` | `rclcpp::shutdown();` |
| Register executable | `setup.py` → `console_scripts` | `CMakeLists.txt` → `add_executable` + `install` |
| Quick test | `chmod +x` + `./file.py` | Must build first |
| Run | `ros2 run my_py_pkg py_node` | `ros2 run my_cpp_pkg cpp_node` |

---

## Workflow Summary

```
1. touch src/my_first_node.cpp     ← create file
2. write the code                   ← init → Node → spin → shutdown
3. edit CMakeLists.txt              ← add_executable + ament_target_dependencies + install
4. colcon build --packages-select   ← from ~/ros2_ws
5. . install/setup.bash             ← refresh environment
6. ros2 run my_cpp_pkg cpp_node     ← run anywhere
```

---

## What's Next

- Refactor the C++ node using **object-oriented programming** (subclass `rclcpp::Node`)
- Add a **timer** — same concept as in Python, with C++ syntax for callbacks