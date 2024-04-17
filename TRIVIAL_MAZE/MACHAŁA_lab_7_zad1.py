import networkx as nx
import random
import matplotlib.pyplot as plt


def node_weight(maze_graph):
    for x, y in maze_graph.edges:
        maze_graph[x][y]['weight'] = random.randint(1, 100)


def solve_maze(maze, startint_point, ending_point):
    path = nx.shortest_path(maze, startint_point, ending_point)
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        x1, y1 = u
        x2, y2 = v
        plt.plot([x1 + 0.5, x2 + 0.5], [y1 + 0.5, y2 + 0.5], 'r', linewidth=2)

    plt.plot([startint_point[0] + 0.5], [startint_point[1] + 0.5], 'bo', markersize=10)
    plt.plot([ending_point[0] + 0.5], [ending_point[1] + 0.5], 'ro', markersize=10)


def generate_perfect_maze(rows, columns):
    maze_graph = nx.grid_2d_graph(rows, columns)
    node_weight(maze_graph)
    minimum_spanning_tree = nx.minimum_spanning_tree(maze_graph)
    maze_graph.remove_edges_from(list(set(maze_graph.edges) - set(minimum_spanning_tree.edges)))
    return maze_graph


def maze_caller_made(maze, startint_point, ending_point):
    positions = {(x, y): (x, y) for x, y in maze.nodes}

    min_x = min(positions.keys(), key=lambda p: p[0])[0]
    max_x = max(positions.keys(), key=lambda p: p[0])[0]
    min_y = min(positions.keys(), key=lambda p: p[1])[1]
    max_y = max(positions.keys(), key=lambda p: p[1])[1]

    plt.plot([min_x, max_x, max_x, min_x, min_x],
             [min_y, min_y, max_y, max_y, min_y], 'k', linewidth=4)

    for u, v in maze.edges:
        x1, y1 = u
        x2, y2 = v
        plt.plot([x1, x2], [y1, y2], 'b', linewidth=2)

    solve_maze(maze, startint_point, ending_point)

    plt.axis('off')
    plt.savefig('maze2.png')
    plt.show()


def draw_maze(maze, start, end):
    positions = {(x, y): (x, y) for x, y in maze.nodes}

    min_x = min(positions.keys(), key=lambda p: p[0])[0]
    max_x = max(positions.keys(), key=lambda p: p[0])[0]
    min_y = min(positions.keys(), key=lambda p: p[1])[1]
    max_y = max(positions.keys(), key=lambda p: p[1])[1]

    plt.plot([min_x + 0.5, max_x + 0.5, max_x + 0.5, min_x + 0.5, min_x + 0.5],
             [min_y + 0.5, min_y + 0.5, max_y + 0.5, max_y + 0.5, min_y + 0.5], 'k', linewidth=4)

    for u, v in maze.edges:
        x1, y1 = u
        x2, y2 = v
        plt.plot([x1 + 0.5, x2 + 0.5], [y1 + 0.5, y2 + 0.5], 'b', linewidth=2)

    plt.plot([start[0] + 1], [start[1] + 1], 'go', markersize=10)
    plt.plot([end[0] + 1], [end[1] + 1], 'ro', markersize=10)

    plt.axis('off')
    plt.savefig('maze.png')
    plt.show()


rows = 25
columns = 20

start = (5, 2)
end = (4, 8)

maze = generate_perfect_maze(rows, columns)
draw_maze(maze, start, end)
maze_caller_made(maze, start, end)
