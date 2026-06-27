# Class 14 — Creating and Setting Up a ROS2 Workspace

## What is a Workspace?

A workspace is just a directory where you write, build, and install all the code for a ROS2 application. It has no special magic — just a folder with a specific structure.

---

## Step 1 — Create the Workspace

```bash
cd ~/Documents/ROS2forBeginners-ROS2Jazzy-2025
mkdir ros2_ws
cd ros2_ws
mkdir src
```

That's it. The only thing needed to initialize a workspace is a `src/` folder inside it. All package code lives here.

```
ros2_ws/
└── src/        ← all your packages go here
```

---

## Step 2 — Build the Workspace

Always build from the **workspace root** (`ros2_ws/`), never from inside `src/`:

```bash
cd ~/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws
colcon build
# Summary: 0 packages finished [6.72s]
```

`colcon` is the build tool for ROS2. After the first build, three new folders are auto-generated:

```
ros2_ws/
├── src/        ← your code
├── build/      ← intermediate build files
├── install/    ← installed outputs & setup scripts
└── log/        ← build logs
```

> If `colcon` is not found, install it:
> ```bash
> sudo apt install ros-dev-tools
> ```

---

## Step 3 — Source the Workspace

After building, source the workspace to make its packages available in the terminal:

```bash
source install/setup.bash
```

`install/setup.bash` sources both the global ROS2 installation **and** this workspace. `local_setup.bash` only sources the workspace — use `setup.bash` to keep things simple.

---

## Step 4 — Add to `.bashrc` (permanent)

Sourcing manually every terminal session is tedious. Add both lines to `~/.bashrc`:

```bash
# Global ROS2 installation (already added in the installation section)
source /opt/ros/jazzy/setup.bash

# Your workspace (add this below the line above)
source ~/Documents/ROS2forBeginners-ROS2Jazzy-2025/ros2_ws/install/setup.bash
```

> ⚠️ Order matters: always source the global ROS2 installation **before** the workspace.

After saving `.bashrc`, every new terminal will have both sourced automatically.

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| `colcon build` run inside `src/` | `cd` to workspace root first, then build |
| Built in wrong place by accident | `rm -rf build install log` then rebuild from workspace root |
| Typo: `cd scr` instead of `cd src` | Double-check folder name (`src`, not `scr`) |

---

## What's Next

- Create Python and C++ packages inside `src/`
- Add nodes to those packages