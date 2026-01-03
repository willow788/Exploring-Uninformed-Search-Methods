# 🌊 Breadth-First Search (BFS)

<div align="center">

**Queue-based level-order graph traversal**

![BFS](https://img.shields.io/badge/Algorithm-BFS-blue?style=for-the-badge)
![Complexity](https://img.shields.io/badge/Space-O(w)-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-NEW-success?style=for-the-badge)

</div>

---

## 📖 What is BFS?

**Breadth-First Search (BFS)** is a graph traversal algorithm that explores nodes level by level, visiting all neighbors at the current depth before moving to nodes at the next depth level. It uses a **queue** (First-In-First-Out) data structure.

### 🎯 Key Characteristics

- **Data Structure:** Queue (FIFO)
- **Exploration Strategy:** Wide before deep (level-by-level)
- **Implementation:** Iterative with queue
- **Space Complexity:** O(w) where w is the maximum width
- **Time Complexity:** O(V + E) where V is vertices and E is edges
- **Completeness:** Yes (for finite graphs)
- **Optimal:** Yes (for unweighted graphs)

---

## 🧠 How BFS Works

### Algorithm Steps

1. **Initialize** a queue with the start node
2. **Mark** the start node as visited
3. **Dequeue** the front node from queue
4. **Process** the current node
5. **Enqueue** all unvisited neighbors
6. **Repeat** steps 3-5 until queue is empty

### Visual Example

```
Graph:      A
           / \
          B   C
         / \   \
        D   E   F

BFS Order: A → B → C → D → E → F

Level 0: A
Level 1: B, C
Level 2: D, E, F
```

The algorithm explores layer by layer, ensuring all nodes at depth *n* are visited before any node at depth *n+1*.

---

## 💻 Implementation

**Location:** `BREADTH FIRST SEARCH/Python code/bfs.py`

### Core Algorithm

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return order
```

---

## 🎨 Advanced Features

### 1️⃣ Random Graph Generation

The BFS implementation includes automatic random graph creation:

```python
def gen_graph(n, p):
    """
    Generate random graph with n nodes
    and edge probability p
    """
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                graph[i].append(j)
                graph[j].append(i)
    return graph
```

**Parameters:**
- `n`: Number of nodes (default: 20)
- `p`: Edge probability (default: 0.2)

---

### 2️⃣ Force-Directed Graph Layout

Implements a **Fruchterman-Reingold** spring layout algorithm for beautiful graph positioning:

```python
def force_directed_positions(graph, radius=16, iterations=250, seed=7):
    """
    Custom implementation of spring layout
    No NetworkX dependency required!
    """
    # Physics-based node positioning
    # Repulsion between all nodes
    # Attraction along edges
    # Iterative refinement
```

**Features:**
- 🌀 Physics-based positioning
- 🎯 No NetworkX dependency
- 🎨 Beautiful, uncluttered layouts
- ⚡ Fast convergence

---

### 3️⃣ Matplotlib Animation

**Stunning visualizations** with:

- 🎬 Real-time animation of BFS traversal
- 🎨 Color-coded node states
- 📊 Professional dark theme
- 🎭 Smooth transitions
- 📈 Queue state visualization

**Color Coding:**
- 🟡 **Yellow** - Current node being explored
- 🟢 **Green** - Visited nodes
- 🔵 **Cyan** - Nodes in queue (frontier)
- ⚪ **Light Gray** - Unvisited nodes

---

## 🎛️ Customizable Parameters

Edit these in `bfs.py`:

```python
# Graph Configuration
num_nodes = 20              # Number of nodes
edge_prob = 0.2             # Edge creation probability (0.0 to 1.0)
start_node = 0              # Starting node for BFS

# Animation Settings
animation_speed = 1200      # Milliseconds per frame (higher = slower)

# Layout Options
use_random_graph = True     # True: random graph, False: predefined
use_force_directed_layout = True  # True: spring layout, False: circular
layout_seed = 7             # Seed for reproducible layouts
random_layout_radius = 16   # Spread of the graph
```

---

## 🚀 Running BFS

### Basic Execution

```bash
cd "BREADTH FIRST SEARCH/Python code"
python bfs.py
```

### Quick Customization

**Small Dense Graph:**
```python
num_nodes = 10
edge_prob = 0.5
animation_speed = 800
```

**Large Sparse Graph:**
```python
num_nodes = 50
edge_prob = 0.1
animation_speed = 500
```

**Custom Test Graph:**
```python
use_random_graph = False
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}
```

---

## 🎯 Use Cases

BFS excels at:

### ✅ Optimal Applications

- 🎯 **Shortest Path** - Unweighted graphs
- 📊 **Level-Order Traversal** - Trees and hierarchies
- 🌐 **Web Crawling** - Limited depth exploration
- 🎮 **Game Boards** - Minimum moves problems
- 🗺️ **GPS Navigation** - Shortest route finding
- 👥 **Social Networks** - Degrees of separation
- 🔄 **Peer-to-Peer Networks** - Broadcasting

### ⚠️ Limitations

- ❌ High memory usage for wide graphs
- ❌ Not suitable for very deep searches
- ❌ Doesn't handle weighted graphs optimally

---

## 🔬 Algorithm Analysis

### Time Complexity

- **All Cases:** O(V + E)
  - V = vertices (nodes)
  - E = edges (connections)

### Space Complexity

- **Queue:** O(w) where w is maximum width
- **Visited Set:** O(V)
- **Total:** O(V + w)

### Comparison

| Graph Type | DFS Memory | BFS Memory |
|------------|------------|------------|
| Balanced Tree (h=10) | O(10) | O(2^9) |
| Long Chain (n=100) | O(100) | O(1) |
| Complete Graph (n=50) | O(50) | O(50) |

---

## 🆚 DFS vs BFS

| Feature | DFS | BFS |
|---------|-----|-----|
| **Data Structure** | Stack | Queue |
| **Exploration** | Depth-first | Level-first |
| **Shortest Path** | ❌ No | ✅ Yes |
| **Space (tree)** | O(h) | O(2^h) |
| **Complete** | ❌ No* | ✅ Yes** |
| **Use Case** | Deep searches | Shallow/shortest |

\* Infinite graphs  
\** Finite graphs

---

## 💡 Key Insights

### When to Use BFS

- 🎯 Finding **shortest path** in unweighted graphs
- 📏 Target is likely **close to start**
- 🌐 **Level-order** processing needed
- 🎮 **Minimum steps** problems
- 👥 **Network distance** calculations

### BFS Variants

- **Bidirectional BFS** - Search from both ends
- **Multi-source BFS** - Multiple starting points
- **0-1 BFS** - Graphs with 0 and 1 weights
- **Parallel BFS** - Distributed graph processing

---

## 🎨 Visualization Features

### What Makes This BFS Special

1. **🎲 Random Graph Generation**
   - Creates diverse test cases automatically
   - Adjustable size and density
   - Reproducible with seeds

2. **🌀 Force-Directed Layout**
   - Custom Fruchterman-Reingold implementation
   - No NetworkX dependency
   - Beautiful, organic-looking graphs

3. **🎬 Smooth Animation**
   - Frame-by-frame BFS execution
   - Clear queue visualization
   - Professional aesthetics

4. **🎛️ Full Customization**
   - Easy parameter tweaking
   - Multiple layout options
   - Flexible graph definitions

---

## 📊 Sample Output

### Console Output (if enabled)

```
Starting BFS from node 0
Queue: [0]
Visiting: 0
Queue: [1, 2]
Visiting: 1
Queue: [2, 3, 4]
...
BFS Complete!
Order: [0, 1, 2, 3, 4, 5, ...]
```

### Visual Output

The matplotlib animation shows:
- 🎨 Graph structure with edges
- 🎭 Color-coded node states
- 📊 Current queue contents
- 🎯 Traversal progress
- 📈 Legend and labels

---

## 🛠️ Technical Details

### Dependencies

```bash
pip install matplotlib numpy
```

**Note:** NetworkX is **NOT required**! This implementation uses:
- Custom force-directed layout
- Native Python data structures
- NumPy for efficient calculations

### Performance

- **Graph Generation:** O(n²) time
- **Layout Calculation:** O(n² × iterations)
- **BFS Traversal:** O(V + E)
- **Animation:** Real-time rendering

---

## 📚 Further Reading

### Papers & Books

- **Russell & Norvig** - *AI: A Modern Approach* (Chapter 3)
- **Cormen et al.** - *Introduction to Algorithms* (Chapter 22)
- **Fruchterman & Reingold** (1991) - Force-directed graph drawing

### Related Documentation

- [Force-Directed Layouts](Force-Directed-Layouts.md) - Deep dive into spring algorithms
- [Visualization Techniques](Visualization-Techniques.md) - Animation best practices
- [Customization Guide](Customization-Guide.md) - Parameter tuning

---

## 🔗 Related Topics

- [Depth-First Search (DFS)](Depth-First-Search.md) - Stack-based alternative
- [Installation & Setup](Installation-and-Setup.md) - Getting started
- [Troubleshooting](Troubleshooting.md) - Common issues

---

<div align="center">

**Navigation:** [← DFS](Depth-First-Search.md) | [Home](Home.md) | [Next: Visualization →](Visualization-Techniques.md)

</div>