# Class 15 — Creating a ROS2 Python Package

## Command to Create the Package

Run this from inside your workspace's `src/` folder:

```bash
cd ~/ros2_ws/src
ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
```

| Option | Value | Purpose |
|---|---|---|
| `--build-type` | `ament_python` | Marks this as a Python package |
| `--dependencies` | `rclpy` | Python client library for ROS2 |

> `ament` is the build system. `colcon` is the build tool. You'll see both throughout the course.

The `[WARNING]` about the license is harmless — only matters if you plan to publish the package publicly (e.g. on GitHub). Ignore it for now.

---

## Package Structure Generated

```
my_py_pkg/
├── my_py_pkg/           ← your Python nodes go here
│   └── __init__.py
├── resource/
│   └── my_py_pkg
├── test/                ← auto-generated tests (ignore for now)
│   ├── test_copyright.py
│   ├── test_flake8.py
│   └── test_pep257.py
├── package.xml          ← package metadata & dependencies (mandatory)
├── setup.py             ← used to install nodes
└── setup.cfg            ← used to install nodes
```

- `my_py_pkg/` (inner folder) → where `.py` node files are written
- `package.xml` → the one mandatory file in every ROS2 package
- `setup.py` / `setup.cfg` → revisited when creating the first node
- `resource/` and `test/` → no need to touch these for now

---

## package.xml — Key Fields

```xml
<name>my_py_pkg</name>
<version>0.0.0</version>
<build_type>ament_python</build_type>
<depend>rclpy</depend>
```

To add more dependencies later, append more `<depend>` tags below the existing one.

---

## Building

Always build from the **workspace root**, not from `src/`:

```bash
cd ~/ros2_ws
colcon build
# Starting >>> my_py_pkg
# Finished <<< my_py_pkg [15.9s]
```

Build a single package (faster during development):

```bash
colcon build --packages-select my_py_pkg
# Starting >>> my_py_pkg
# Finished <<< my_py_pkg [7.14s]
```

> ⚠️ Never run `colcon build` inside `src/`. If you do by mistake, delete the generated folders and retry:
> ```bash
> rm -rf build install log   # run this inside src/ to undo
> cd ~/ros2_ws
> colcon build
> ```

---

## Opening VSCode

Always open VSCode from the `src/` folder — this ensures correct Autocompletion for imports:

```bash
cd ~/ros2_ws/src
code .
```

---

## What's Next

- Create the first Python node inside `my_py_pkg/my_py_pkg/`
- Register the node in `setup.py`
- Run and inspect nodes with command-line tools