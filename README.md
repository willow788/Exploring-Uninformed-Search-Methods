# 🔍 Exploring Uninformed Search Methods

### *A Visual Journey Through AI Search Algorithms*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/Artificial_Intelligence-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

This repository contains approachable, well-documented implementations and visualizations of foundational uninformed search algorithms. The goal is to teach algorithm mechanics through minimal examples, console tracing, and animated visualizations.

---

## 🎯 What's Inside

### ✅ Current Implementations

- 🌳 Depth-First Search (DFS)
  - Minimal Python implementation (recursive)
  - Console visual version with step-by-step tracing
  - Matplotlib animated visualization (colored node states)
- 🌊 Breadth-First Search (BFS)
  - Python implementation with Matplotlib animation
  - Random graph generation and force-directed layout support
- 🔁 Depth-Limited Search (DLS) — NEW
  - DFS variation with a depth cutoff to prevent exploring beyond a given depth
  - Console and visual examples
- 🔂 Iterative Deepening Search (IDS) — NEW
  - Repeated depth-limited searches with increasing depth limits
  - Combines DFS space efficiency with BFS completeness up to the limit

(Planned — coming soon)
- Uniform Cost Search (UCS)
- Bidirectional Search

---

## 🚀 What's New

- Added Depth-Limited Search (DLS):
  - Implementation with a configurable depth limit
  - Useful for search problems with known depth bounds or to avoid infinite exploration
- Added Iterative Deepening Search (IDS):
  - Implementation that repeatedly runs DLS with increasing depth limits
  - Retains memory efficiency of DFS while being complete for finite-depth goals
- Updated README to document DLS and IDS, their locations, usage, and configuration options
- BFS implementation and visual improvements remain included

---

## 📂 Repository Structure (high level)

```
Exploring-Uninformed-Search-Methods/
├── DEPTH FIRST SEARCH/
│   ├── minimal Python code/
│   ├── DFS with Visuals/
│   ├── DFS using Matplotlib/
│   ├── Depth-Limited Search/         # DLS (new)
│   │   └── Python code/
│   └── Iterative Deepening Search/   # IDS (new)
│       └── Python code/
├── BREADTH FIRST SEARCH/
│   └── Python code/
├── docs/
├── README.md
└── LICENSE
```

---

## 🛠️ Installation & Requirements

Prerequisites:
- Python 3.7+

Recommended packages:
```bash
pip install matplotlib numpy
# Optional (used by some DFS examples)
pip install networkx
```

---

## 🧭 Running the Examples

All examples are runnable as simple Python scripts. Copy the commands below to try them locally.

### Depth-First Search

Minimal implementation:
```bash
cd "DEPTH FIRST SEARCH/minimal Python code"
python main.py
```

Console visualization:
```bash
cd "DEPTH FIRST SEARCH/DFS with Visuals/Python code"
python main.py
```

Matplotlib animation:
```bash
cd "DEPTH FIRST SEARCH/DFS using Matplotlib/Python code"
python main.py
```

### Breadth-First Search (BFS)

Run the BFS animation:
```bash
cd "BREADTH FIRST SEARCH/Python code"
python bfs.py
```

### Depth-Limited Search (DLS) — NEW

Run the DLS example/visual:
```bash
cd "DEPTH FIRST SEARCH/Depth-Limited Search/Python code"
python main.py
```

Typical DLS configuration (edit at top of the script):
```python
depth_limit = 3      # Maximum depth to explore from the start node
start_node = 0       # Starting node index
# Other parameters may include graph size and layout options
```

Behavior:
- The search will not expand nodes deeper than depth_limit.
- Useful for preventing infinite exploration in cyclic or infinite graphs.

### Iterative Deepening Search (IDS) — NEW

Run the IDS example/visual:
```bash
cd "DEPTH FIRST SEARCH/Iterative Deepening Search/Python code"
python main.py
```

Typical IDS configuration:
```python
max_depth = 6        # Maximum depth to attempt (stops earlier if goal found)
start_node = 0
# Optional: step size or timeout between iterations for animation clarity
```

Behavior:
- IDS runs DLS repeatedly with depth limits 0,1,2,... until the goal is found or max_depth is reached.
- IDS combines memory efficiency of DFS with the completeness of BFS (up to the depth explored).

---

## 🎨 Visuals & Color Legend

The Matplotlib visualizations use a consistent legend across examples:

- 🟠 Amber — Current node being processed
- 🟢 Green — Visited nodes
- 🔵 Blue — Nodes in the frontier (stack for DFS / queue for BFS)
- ⚫ Gray — Unvisited nodes

Animations show the algorithm's frontier, visited set progression, and the current step — designed for teaching and intuitive understanding.

---

## 💻 Implementation Notes

- DFS and DLS use recursive or stack-based strategies to illustrate depth-first behavior.
- DLS enforces a depth cutoff; IDS repeatedly increases that cutoff.
- BFS uses a queue and includes random graph generation plus a force-directed layout for pleasing visuals.
- Visualizations are intentionally lightweight and dependency-minimal (custom spring layout provided so NetworkX is optional).

---

## 📚 Documentation

A short set of docs is provided in the `docs/` folder:
- `docs/Home.md` — Project overview and quick start
- `docs/Depth-First-Search.md` — Detailed DFS explanations and examples (updated to reference DLS and IDS)
- `docs/Breadth-First-Search.md` — BFS design notes and visualization details

Visit the `docs/` folder for step-by-step guidance and example code snippets.

---

## 🎓 Learning Objectives

- Understand how DFS, DLS, IDS and BFS explore search spaces differently
- See the difference between stack-based (DFS/DLS/IDS) and queue-based (BFS) frontiers
- Observe how graph structure and layout affect visualization
- Learn to instrument and visualize algorithm state for debugging and teaching

### 🔬 Quick comparison

| Aspect | DFS | DLS | IDS | BFS |
|--------|-----|-----|-----|-----|
| Data Structure | Stack / recursion | Stack + depth cutoff | Repeated DLS | Queue |
| Completeness | Not guaranteed | Not guaranteed beyond cutoff | Complete up to max depth | Complete (finite graphs) |
| Memory | Low (O(h)) | Low (O(lim)) | Low (O(lim)) | Higher (O(width)) |
| Use case | Deep exploration | Bounded depth problems | Unknown depth, memory constrained | Shortest-path in unweighted graphs |

---

## 👤 Credits

**Code & Implementation**
- [@willow788](https://github.com/willow788) — Core algorithms, visualizations, and project structure

**Design & Visual Enhancements**
- GitHub Copilot — Matplotlib styling and animation helpers (contributions to styling, comments, and README iteration)

---

## 📚 References

- Russell, S., & Norvig, P. _Artificial Intelligence: A Modern Approach_
- Fruchterman, T. M., & Reingold, E. M. (1991). Graph Drawing by Force-directed Placement
- Matplotlib documentation: https://matplotlib.org/
- NumPy documentation: https://numpy.org/

---

## 📝 License

This project is released under the MIT License. See the LICENSE file for details.

---


