#here we are trying to implement depth limited search algorithm in python
import matplotlib.pyplot as plt

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]

]

initial_position = (0, 0)  # starting point
goal_position = (4, 4)     # goal point


class Problem:
    def __init__(self, grid, initial, goal):
        self.grid = grid
        self.initial = initial
        self.goal = goal

    def is_goal(self, position):
        return position == self.goal
    
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


# Global visualize_path function
def visualize_path(grid, path):
    fig, ax = plt.subplots()
    nrows, ncols = len(grid), len(grid[0])
    ax.set_xticks([x - 0.5 for x in range(1, ncols)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, nrows)], minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    ax.imshow(grid, cmap='Greys', interpolation='none')

    #highlight the path
    if path:
        for (x, y) in path:
            ax.add_patch(plt.Circle((y,x), radius=0.3, color='red'))

    #highlight start and goal positions
    ax.add_patch(plt.Circle((initial_position[1], initial_position[0]), radius=0.3, color='green'))
    ax.add_patch(plt.Circle((goal_position[1], goal_position[0]), radius=0.3, color='blue'))
    plt.gca().invert_yaxis()
    plt.title("Depth Limited Search Path Visualization")
    plt.show()
    def __init__(self, grid, initial, goal):
        self.grid = grid
        self.initial = initial
        self.goal = goal

    def is_goal(self, position):
        return position == self.goal
    
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
    


def depth_limited_search(node, goal_test, limit):
    if goal_test(node):
        return node
    elif limit == 0:
        return "cutoff"
    else:
        cutoff_occured = False
        for child in expand(node):
            result = depth_limited_search(child, goal_test, limit - 1)
            if result == "cutoff":
                cutoff_occured = True
            elif result != "failure":
                return result
        return "cutoff" if cutoff_occured else "failure"
    


problem = Problem(grid, initial_position, goal_position)


# Helper function to wrap expand and goal_test for the search
def goal_test(position):
    return problem.is_goal(position)

def expand(position):
    return problem.expand(position)

# Modified DLS to return path
def depth_limited_search_path(node, goal_test, limit, path=None):
    if path is None:
        path = [node]
    if goal_test(node):
        return path
    elif limit == 0:
        return "cutoff"
    else:
        cutoff_occured = False
        for child in expand(node):
            if child not in path:  # avoid cycles
                result = depth_limited_search_path(child, goal_test, limit - 1, path + [child])
                if result == "cutoff":
                    cutoff_occured = True
                elif result != "failure":
                    return result
        return "cutoff" if cutoff_occured else "failure"

depth_limited = 10
path = depth_limited_search_path(problem.initial, goal_test, depth_limited)


if path == "failure":
    print("No solution found within depth limit")
elif path == "cutoff":
    print("Cutoff occurred, depth limit reached")
else:
    print("Path to goal:", path)
    visualize_path(grid, path)







