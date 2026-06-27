# Class 11 — Running Your First ROS2 Program

## Goal

Validate that ROS2 is correctly installed and sourced by running two pre-installed example nodes that communicate with each other. No code is written here.

---

## Terminal 1 — Run the Talker

```bash
ros2 run demo_nodes_cpp talker
```

Expected output:

```
[INFO] [...] Publishing: 'Hello World: 1'
[INFO] [...] Publishing: 'Hello World: 2'
[INFO] [...] Publishing: 'Hello World: 3'
...
```

---

## Terminal 2 — Run the Listener

```bash
ros2 run demo_nodes_cpp listener
```

Expected output:

```
[INFO] [...] I heard: 'Hello World: 40'
[INFO] [...] I heard: 'Hello World: 41'
...
```

The numbers printed by the listener match those published by the talker — this confirms the two nodes are communicating.

---

## What is Happening

| Node | Package | Role |
|---|---|---|
| `talker` | `demo_nodes_cpp` | Publishes "Hello World: N" messages |
| `listener` | `demo_nodes_cpp` | Receives and prints those messages |

This is the classic publisher/subscriber pattern in ROS2. The two nodes run in separate terminals (separate processes) and communicate through ROS2. You will implement this pattern yourself later in the course.

---

## Stopping a Node

Press `Ctrl+C` in the terminal running the node. Each node stops independently — stopping the talker means the listener receives nothing, but it keeps running without crashing.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `Package 'demo_nodes_cpp' not found` | ROS2 environment not sourced | Run `source /opt/ros/jazzy/setup.bash` or check `.bashrc` |
| Listener receives nothing | Talker not running | Make sure the talker terminal is active |
| Any other error | Installation issue | Revisit the installation lessons |

---

## What's Next

- Understand what packages and nodes are
- Create your own workspace, packages, and nodes