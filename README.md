# ROS 2 Turtlesim Controller

Drives the turtlesim turtle in a repeating straight-then-turn pattern by publishing `geometry_msgs/Twist` at 10 Hz. Speed and topic are parameters.

## Packages

- `turtle_control` (ament_python): `turtle_controller`

## Requirements

- Ubuntu 24.04, ROS 2 Jazzy
- `turtlesim` (`sudo apt install ros-jazzy-turtlesim`)

## Build

```bash
cd turtle_ws
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```

## Run

Source `install/setup.bash` in every new terminal first.

```bash
# Terminal 1
ros2 run turtlesim turtlesim_node

# Terminal 2
ros2 run turtle_control turtle_controller

# With parameters
ros2 run turtle_control turtle_controller --ros-args -p speed:=1.0
```

## Concepts practised

velocity commands, timers, parameters
