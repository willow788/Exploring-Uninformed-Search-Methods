import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patheffects as pe
from collections import deque
import numpy as np
import random

#initialize graph parameters
num_nodes = 20
edge_prob = 0.2
start_node = 0
animation_speed = 1200 # milliseconds (higher = slower)
random_layout_radius = 16
use_random_graph = True
layout_seed = 7
use_force_directed_layout = True

# Generate a random graph
def gen_graph(n, p):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                graph[i].append(j)
                graph[j].append(i)


    return graph

#adding in a defailt graph for testing
if use_random_graph:
    graph = gen_graph(num_nodes, edge_prob)
else:
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }

length = len(graph)

# layout helpers
def _edges_undirected(graph):
    edges = set()
    for u, nbrs in graph.items():
        for v in nbrs:
            if u == v:
                continue
            a, b = (u, v) if u < v else (v, u)
            edges.add((a, b))
    return list(edges)


def force_directed_positions(graph, radius=16, iterations=250, seed=7):
    """Small, dependency-free spring layout (Fruchterman–Reingold style).

    Good enough for n~20-200 and avoids clustered random placements.
    """
    rng = np.random.default_rng(seed)
    nodes = sorted(graph.keys())
    n = len(nodes)
    if n == 0:
        return {}

    node_to_idx = {node: i for i, node in enumerate(nodes)}
    edges = _edges_undirected(graph)

    # start in a rough circle with slight jitter (prevents symmetry lock)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    pos = np.stack([np.cos(angles), np.sin(angles)], axis=1)
    pos += rng.normal(scale=0.05, size=pos.shape)

    # FR constants
    k = np.sqrt(1.0 / n)
    temperature = 0.15

    for it in range(iterations):
        disp = np.zeros((n, 2), dtype=float)

        # repulsion (all pairs)
        for i in range(n):
            delta = pos[i] - pos
            dist = np.linalg.norm(delta, axis=1) + 1e-9
            # ignore self; delta[ i ] is zero anyway
            force = (k * k) / dist
            disp[i] += np.sum((delta / dist[:, None]) * force[:, None], axis=0)

        # attraction (edges)
        for u, v in edges:
            iu = node_to_idx[u]
            iv = node_to_idx[v]
            delta = pos[iu] - pos[iv]
            dist = np.linalg.norm(delta) + 1e-9
            force = (dist * dist) / k
            vec = (delta / dist) * force
            disp[iu] -= vec
            disp[iv] += vec

        # limit movement, cool down
        t = temperature * (1.0 - (it / iterations))
        for i in range(n):
            d = np.linalg.norm(disp[i]) + 1e-9
            pos[i] += (disp[i] / d) * min(d, t)

        # keep centered
        pos -= np.mean(pos, axis=0)

    # scale to radius
    max_norm = np.max(np.linalg.norm(pos, axis=1)) + 1e-9
    pos = (pos / max_norm) * radius

    return {node: (float(pos[node_to_idx[node], 0]), float(pos[node_to_idx[node], 1])) for node in nodes}


if use_force_directed_layout:
    positions = force_directed_positions(graph, radius=random_layout_radius, seed=layout_seed)
else:
    angles = [2 * 3.14159 * i / len(graph) for i in range(len(graph))]
    positions = {
        i: (
            random_layout_radius * random.uniform(-1, 1),
            random_layout_radius * random.uniform(-1, 1),
        )
        for i in graph
    }

#bfs state generator
def bfs_states(graph, start):
    visited = set()
    queue = deque([start])
    edge_states = set()

    while queue:
        current = queue[0]
        current_frontier = list(queue)
        yield visited.copy(), current_frontier.copy(), edge_states.copy()

        node = queue.popleft()

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                edge_states.add((min(node, neighbor), max(node, neighbor)))

        yield visited.copy(), list(queue), edge_states.copy()

#plotting and animation


fig, ax = plt.subplots()
fig.patch.set_facecolor('black')

# match axis background too
ax.set_facecolor('black')


#this forces equal scaling in both directions
ax.set_aspect('equal')

#this turns off the axis
ax.axis('off')

#setting the title
ax.set_title('BFS Traversal Animation', color='white')

#draw edges

#initialize edge artists which is empty right now
edge_artists = {}

#loops thought every node u in the graph
for u in graph:

    #loops through the connected nodes v of u
    for v in graph[u]:

        #avoid drawing the same edge twice
        if (v, u)  in edge_artists:
            continue

        #draw the edge between nodes u and v
        x1, y1 = positions[u]
        x2, y2 = positions[v]

        #create a line artist for the edge by grabbing the coordinates of the two nodes
        artist = ax.plot([x1, x2], [y1, y2], color='#404040', linewidth=1.6, alpha=0.9, zorder=1)[0]

        #storing the artist in the edge_artist dictionary with the edge tuple as the key
        edge_artists[u, v] = artist

#draw nodes

#initialize node artists which is empty right now
node_artists = {}

#loops through every node in the graph

degrees = {node: len(graph[node]) for node in graph}

for node, (x, y) in positions.items():

    #drawing a circle for each node
    # slightly scale node size by degree for readability
    size = 260 + 35 * degrees.get(node, 0)
    artist = ax.scatter(x, y, s=size, color='#A8A8A8', edgecolors='white', linewidths=1.2, zorder=2)

    #sorting the artist in the node_artist dictionary with the node as the key
    node_artists[node] = artist

    #adding text labels to the nodes
    #the text label is the node number

    label = ax.text(x, y, str(node), color='white', fontsize=10, ha='center', va='center', zorder=3)
    label.set_path_effects([pe.Stroke(linewidth=3, foreground='black'), pe.Normal()])

#prepare bfs states for animation
states = list(bfs_states(graph, start_node))




#animation update function
def update(frame):

    #get the current state
    visited, frontier, edge_states = states[frame]


    #update node colors based on their state
    for node, artist in node_artists.items():

        #check if the node is visited, in the frontier, or unvisited
        if node in visited:
            artist.set_color("#2ECC71")  # visited
        elif node in frontier:
            artist.set_color("#F39C12")  # frontier
        else:
            artist.set_color("#8A8A8A")  # unvisited


#update edge colors based on their state

    for (u, v), artist in edge_artists.items():

        #check if the edge is in the explored edge states

        if (u, v) in edge_states:
            artist.set_color("#00C2FF")
            artist.set_linewidth(2.6)
            artist.set_alpha(0.95)
        else:
            artist.set_color("#404040")
            artist.set_linewidth(1.6)
            artist.set_alpha(0.7)

    # keep a consistent view box with padding
    pad = 2.8
    xs = [p[0] for p in positions.values()]
    ys = [p[1] for p in positions.values()]
    ax.set_xlim(min(xs) - pad, max(xs) + pad)
    ax.set_ylim(min(ys) - pad, max(ys) + pad)

#create the animation   
ani = FuncAnimation(fig, update, frames=len(states), interval=animation_speed, repeat=False)

plt.show()
