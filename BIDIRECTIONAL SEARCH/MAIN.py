
import networkx  as nx
import heapq
import matplotlib.pyplot as plt
import numpy as np

#implementation of bidirectional uniform cost search
from collections import deque

def is_valid_move(x, y, maze):
    rows, cols = maze.shape
    return 0 <= x < rows and 0 <= y < cols and maze[x, y] == 0

def bfs(queue, visited, parent):
    (x, y) = queue.popleft()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dx, dy in directions:
        nx_, ny_ = x + dx, y + dy
        if is_valid_move(nx_, ny_, maze) and (nx_, ny_) not in visited:
            queue.append((nx_, ny_))
            visited.add((nx_, ny_))
            parent[(nx_, ny_)] = (x, y)


def bidirectional_bfs(maze, start, goal):
    if maze[start] == 1 or maze[goal] == 1:
        return None, None, None  # Start or goal is blocked

    start_queue = deque([start])
    goal_queue = deque([goal])

    start_visited = {start}
    goal_visited = {goal}

    start_parent = {start: None}
    goal_parent = {goal: None}

    while start_queue and goal_queue:
        bfs(start_queue, start_visited, start_parent)
        bfs(goal_queue, goal_visited, goal_parent)

        intersection = start_visited.intersection(goal_visited)
        if intersection:
            meet_point = intersection.pop()
            return meet_point, start_parent, goal_parent

    return None, None, None  # No path found

def reconstruct_path(came_from, current):
    total_path = []
    while current is not None:
        total_path.append(current)
        current = came_from.get(current)
    return total_path[::-1]  # Return reversed path

def visualize(maze, path, start, goal):
    maze_copy = np.array(maze)
    fig, ax = plt.subplots(figsize=(10, 10))
    rows, cols = maze_copy.shape
    # Use a visually appealing colormap for the maze
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(['#f8f8ff', '#22223b'])  # light for open, dark for wall
    ax.imshow(maze_copy, cmap=cmap, origin='upper')

    # Draw the path as a thick colored line
    if path:
        path_y = [y + 0.5 for (y, x) in path]
        path_x = [x + 0.5 for (y, x) in path]
        ax.plot(path_x, path_y, color='#ffd700', linewidth=8, alpha=0.8, solid_capstyle='round', zorder=3, label='Path')
        # Overlay path cells for extra highlight
        for (y, x) in path:
            ax.add_patch(plt.Rectangle((x, y), 1, 1, color='#ffe066', alpha=0.5, zorder=2))

    # Mark start and goal with larger, distinct markers
    sy, sx = start
    gy, gx = goal
    ax.scatter([sx+0.5], [sy+0.5], s=300, c='#38b000', marker='o', edgecolors='black', linewidths=2, zorder=4, label='Start')
    ax.scatter([gx+0.5], [gy+0.5], s=300, c='#d90429', marker='*', edgecolors='black', linewidths=2, zorder=4, label='Goal')

    # Set limits, grid, and ticks
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_xticks(np.arange(0, cols+1, 1))
    ax.set_yticks(np.arange(0, rows+1, 1))
    ax.grid(which='both', color='#adb5bd', linewidth=1.5, alpha=0.7)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Add legend and title
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), loc='upper left', fontsize=14, frameon=True, facecolor='white')
    ax.set_title('Bidirectional BFS Maze Path', fontsize=22, color='#22223b', pad=20)

    plt.tight_layout()
    plt.show()



# Define the maze as a numpy array
maze = np.array([
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
])

start = (0, 0)
goal = (4, 4)

intersect_node, parent_start, parent_goal = bidirectional_bfs(maze, start, goal)
if intersect_node is not None:
    # Reconstruct path from start to intersection
    path1 = reconstruct_path(parent_start, intersect_node)
    # Reconstruct path from goal to intersection (reverse, skip intersection)
    path2 = reconstruct_path(parent_goal, intersect_node)[::-1][1:]
    path = path1 + path2
else:
    path = None
visualize(maze, path, start, goal)
