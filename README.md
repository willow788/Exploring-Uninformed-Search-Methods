<div align="center">

# 🔍 Exploring Uninformed Search Methods

### *A Visual Journey Through AI Search Algorithms*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/Artificial_Intelligence-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-2C5F2D?style=for-the-badge&logo=python&logoColor=white)

*Implementations inspired by **Artificial Intelligence:  A Modern Approach***

---

</div>

## 📚 About This Project

This repository is a collection of **uninformed search algorithm** implementations created as part of my AI class journey. Each algorithm is implemented with three different approaches to help learners understand the concepts from basic to advanced visualization.

> 💡 **Learning Resource:** These implementations are based on concepts from *Artificial Intelligence: A Modern Approach* by Stuart Russell and Peter Norvig. 

---

## 🎯 What's Inside

### Current Implementations

#### 🌳 **Depth-First Search (DFS)**

Three progressive implementations to build your understanding:

1. **📝 Minimal Python Code**
   - Clean, recursive DFS implementation
   - Perfect for understanding the core algorithm
   - No external dependencies

2. **🖥️ DFS with Visuals**
   - Stack trace visualization
   - Console output showing visited nodes
   - Step-by-step execution logging

3. **📊 DFS using Matplotlib**
   - Beautiful graph visualization with NetworkX
   - Real-time animated search process
   - Color-coded nodes showing algorithm state: 
     - 🟠 **Amber** - Current node being processed
     - 🟢 **Green** - Visited nodes
     - 🔵 **Blue** - Nodes in the frontier (stack)
     - ⚫ **Gray** - Unvisited nodes

---

## 🚀 Coming Soon

Additional uninformed search methods will be added following the same three-tier approach:

- [ ] **Breadth-First Search (BFS)**
- [ ] **Uniform Cost Search (UCS)**
- [ ] **Depth-Limited Search (DLS)**
- [ ] **Iterative Deepening Search (IDS)**
- [ ] **Bidirectional Search**

> ⏰ *Expected completion: This week*

---

## 🎨 Features

- ✨ **Progressive Learning**: From minimal code to full visualization
- 📖 **Well-Documented**: Clear comments explaining each step
- 🎭 **Beautiful Visuals**: Dark-themed, professional matplotlib outputs
- 🔄 **Animated Algorithms**: Watch the search unfold in real-time
- 🧠 **Educational Focus**: Built for learning and understanding

---

## 🛠️ Installation & Usage

### Prerequisites

```bash
# For visualization examples
pip install matplotlib networkx
```

### Running the Examples

#### Minimal Implementation
```bash
cd "DEPTH FIRST SEARCH/minimal Python code"
python main.py
```

#### With Console Visualization
```bash
cd "DEPTH FIRST SEARCH/DFS with Visuals/Python code"
python main.py
```

#### With Matplotlib Animation
```bash
cd "DEPTH FIRST SEARCH/DFS using Mathplotlib /Python code"
python main.py
```

---

## 📖 Example Output

### Console Visualization
```
Visiting node: A
Stack that are visited: ['C', 'B']
visited nodes in the order: ['A']
-----
Visiting node: B
Stack that are visited: ['C', 'E', 'D']
visited nodes in the order: ['A', 'B']
-----
```

### Matplotlib Visualization
The animated visualization shows:
- **Graph structure** with directed edges
- **Node states** with color coding
- **Step-by-step progression** through the search space
- **Legend** explaining node colors

---

## 🎓 Learning Context

These implementations were created as part of my **Artificial Intelligence** coursework, focusing on understanding search algorithms from first principles. The goal is to provide multiple perspectives on the same algorithm: 

1. **Understand** the logic (minimal code)
2. **Trace** the execution (console output)
3. **Visualize** the process (graphical animation)

---

## 👤 Credits

### Code & Implementation
**[@willow788](https://github.com/willow788)**
- Core algorithm logic
- All DFS implementations
- Project structure and organization

### Design & Visual Enhancements
**GitHub Copilot**
- Matplotlib styling and aesthetics
- Animation improvements
- Code documentation

---

## 📚 References

- **Russell, S., & Norvig, P.** *Artificial Intelligence: A Modern Approach*
- [NetworkX Documentation](https://networkx.org/)
- [Matplotlib Documentation](https://matplotlib.org/)

---

## 📝 License

This project is open source and available for educational purposes.

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**Happy Learning!  🎓**

</div>
