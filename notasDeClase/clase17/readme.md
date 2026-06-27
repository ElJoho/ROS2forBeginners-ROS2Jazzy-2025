# ROS2 Nodes — Class 17

## Definition

A **node** is a subprogram of your application responsible for **one single purpose**. Nodes are written in Python or C++ and live inside packages. They communicate with each other using ROS2 communication tools (topics, services, parameters, etc.).

> Analogy: just like a class in OOP serves a single purpose, a node does too. Two functionalities → two nodes.

---

## Architecture Example

A typical robot application is split into packages, each containing nodes:

| Package | Nodes |
|---|---|
| **Camera** | `camera_driver`, `image_processing` |
| **Motion Planning** | `motion_planning`, `path_correction` |
| **Hardware Control** | `motor_driver` + control loop, `state_publisher` |

Communication flow:
- `image_processing` → `path_correction` (environment analysis)
- `motion_planning` → `motor_driver` (computed trajectories)
- `state_publisher` → `motion_planning` + `path_correction` (hardware status)

> Note: deciding whether two nodes belong in the same package can be tricky. A useful rule — if nodes share common dependencies and are tightly related, group them together.

---

## Key Characteristics & Benefits

**Reduced complexity** — separating your app into nodes makes it easier to scale and maintain. A single monolithic block of code becomes increasingly hard to extend over time.

**Fault tolerance** — nodes run in separate processes. If one crashes, the others keep running. This is especially valuable when a well-tested hardware node must stay alive while you test a new experimental node alongside it.

**Language agnostic** — you can mix Python and C++ nodes freely. They communicate without issues. Common pattern: develop most nodes in Python, write performance-critical nodes in C++.

---

## Important Rules

- Two nodes **cannot share the same name**.
- To run multiple instances of the same node: rename them or place them in different **namespaces**.

---

## What's Next

- Creating nodes in Python and C++
- Using nodes with command-line tools
- Making nodes communicate (topics, services, parameters)