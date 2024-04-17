import random
import networkx as nx
import matplotlib.pyplot as plt


def generate_perfect_maze_with_border(m, n):
    GRAPH = nx.grid_2d_graph(m, n)

    start_node = (random.randint(0, m - 1), random.randint(0, n - 1))

    stack = [start_node]
    visited = set()

    while stack:
        current_node = stack[-1]
        visited.add(current_node)
        unvisited_neighbors = [neighbor for neighbor in GRAPH.neighbors(current_node) if neighbor not in visited]
        if unvisited_neighbors:
            next_node = random.choice(unvisited_neighbors)
            GRAPH.remove_edge(current_node, next_node)

            stack.append(next_node)
        else:
            stack.pop()


    border_nodes = [(x, y) for x in range(m) for y in range(n) if x == 0 or x == m-1 or y == 0 or y == n-1]
    for node in border_nodes:
        GRAPH.add_node(node)

    return GRAPH


m = 10
n = 10

maze = generate_perfect_maze_with_border(m, n)

pos = {(x, y): (x, y) for x in range(m) for y in range(n)}
plt.figure(figsize=(m, n))

for u, v in maze.edges:
    x1, y1 = u
    x2, y2 = v
    plt.plot([x1, x2], [y1, y2], 'k', linewidth=2)

plt.axis('off')
plt.show()