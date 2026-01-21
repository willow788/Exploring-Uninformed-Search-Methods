#now we are trying to implement iterativr deeping search algorithm in python

import matplotlib.pyplot as plt

#defining the grid
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

initial_position = (0, 0)  # starting point
goal_position = (4, 4)     # goal point
cut_off_depth = 10        # maximum depth limit

class Problem:
    def __init__(self, grid, initial, goal):
        self.grid = grid
        self.initial = initial
        self.goal = goal
    def is_goal(self, position):
        return position == self.goal
    
    def is_cycle(self, position, path):
        return position in path
    
    def expand(self, position):
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        result = []
        for move in moves:
            new_position = (position[0] + move[0], position[1] + move[1])
            if (0 <= new_position[0] < len(self.grid) and
                0 <= new_position[1] < len(self.grid[0]) and
                self.grid[new_position[0]][new_position[1]] == 0):
                result.append(new_position)
        return result
    
problem = Problem(grid, initial_position, goal_position)
    

def iterative_deepening_search(problem, cut_off_depth):
    for depth in range(cut_off_depth):
        result = depth_limited_search(problem, depth)
        if result != "cutoff" and result != "failure":
            return result
    return "failure"


def depth_limited_search(problem, limit):
    # defining a frontier stack as it follows LIFO
    frontier = [(problem.initial, 0, [problem.initial])]  # (node, depth, path)
    result = "failure"
    while frontier:
        node, node_depth, path = frontier.pop()
        if problem.is_goal(node):
            return path
        if node_depth > limit:
            result = "cutoff"
        else:
            for child in problem.expand(node):
                if not problem.is_cycle(child, path):
                    frontier.append((child, node_depth + 1, path + [child]))
    return result

       

#visualization of the grid and path
# Global visualize_path function
def visualize_path(grid, path):
    import matplotlib.patches as mpatches
    fig, ax = plt.subplots(figsize=(7, 7))
    nrows, ncols = len(grid), len(grid[0])
    ax.set_xticks([x - 0.5 for x in range(1, ncols)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, nrows)], minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    # Show obstacles as black, free as white
    ax.imshow(grid, cmap='gray_r', interpolation='none')

    # highlight the path
    if path:
        for idx, (x, y) in enumerate(path):
            if (x, y) == initial_position:
                ax.add_patch(plt.Circle((y, x), radius=0.3, color='blue', label='Start' if idx == 0 else None, zorder=3))
                ax.text(y, x, 'S', color='white', ha='center', va='center', fontsize=14, fontweight='bold', zorder=4)
            elif (x, y) == goal_position:
                ax.add_patch(plt.Circle((y, x), radius=0.3, color='green', label='Goal', zorder=3))
                ax.text(y, x, 'G', color='white', ha='center', va='center', fontsize=14, fontweight='bold', zorder=4)
            else:
                ax.add_patch(plt.Circle((y, x), radius=0.25, color='red', alpha=0.7, label='Path' if idx == 1 else None, zorder=2))

    # highlight obstacles
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 1:
                ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, color='black', alpha=0.7, label='Obstacle' if (i == 0 and j == 1) else None, zorder=1))

    plt.gca().invert_yaxis()
    plt.title("Iterative Deepening Search Path Visualization")
    # Create custom legend
    legend_elements = [
        mpatches.Patch(color='white', label='Free Space', edgecolor='black'),
        mpatches.Patch(color='black', label='Obstacle'),
        mpatches.Patch(color='red', label='Path'),
        mpatches.Patch(color='blue', label='Start'),
        mpatches.Patch(color='green', label='Goal')
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.show()
    print("Legend: Blue = Start, Green = Goal, Red = Path, Black = Obstacle, White = Free Space")

# Main execution block
if __name__ == "__main__":
    result = iterative_deepening_search(problem, cut_off_depth)
    if isinstance(result, list) and len(result) > 1:
        print(f"Goal found! Path: {result}")
        print(f"Path length: {len(result)-1}")
        visualize_path(grid, result)
    elif result == "cutoff":
        print("Search was cut off (depth limit reached, no solution found within limit).")
    else:
        print("No solution found.")

#black box is showing the path from initial to goal position
#green circle is the end position
#red circle is the start position
