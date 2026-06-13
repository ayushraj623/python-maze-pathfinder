# 🧭 Maze Pathfinding Visualizer

A terminal-based pathfinding visualizer built in Python. This project visually demonstrates how search algorithms navigate through a 2D grid to find the shortest path from a start point to an end point.

## 🚀 Features
* **Algorithmic Search:** Utilizes Python's `queue` module to implement a Breadth-First Search (BFS) algorithm, guaranteeing the shortest path is found.
* **Real-Time Visualization:** Animates the algorithm's search process step-by-step using the `time` module, allowing users to watch the computer "think."
* **Graphical Terminal UI:** Built using the `curses` library to paint and color the terminal output dynamically (e.g., coloring the path, walls, and start/end nodes).

## 📋 Prerequisites
Ensure you have Python installed on your system (Python 3.x).

* **Windows Users:** The `curses` module is not native to Windows. You must install the `windows-curses` library to run this script:
  ```bash
  pip install windows-curses
