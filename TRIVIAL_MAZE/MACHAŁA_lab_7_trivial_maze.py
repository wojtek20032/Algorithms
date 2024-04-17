import networkx as nx
import matplotlib.pyplot as plt


def node_weight_on_one(maze_graph):
    for x, y in maze_graph.edges:
        maze_graph[x][y]['weight'] = 1


def create_paths(columns, rows, maze_graph):
    for y in range(columns - 2):
        start_node = (0, y)
        end_node = (rows - 1, y + 1)
        if maze_graph.has_edge(start_node, end_node):
            maze_graph[start_node][end_node]['weight'] = 2
            for x in range(1, rows - 1):
                upper_node = (x, y)
                lower_node = (x, y + 1)
                if maze_graph.has_edge(upper_node, lower_node):
                    maze_graph[upper_node][lower_node]['weight'] = 2
                    maze_graph[lower_node][upper_node]['weight'] = 2  # Dodaj odwrotną krawędź


def generate_trivial_maze(rows, columns):
    maze_graph = nx.grid_2d_graph(rows, columns)
    node_weight_on_one(maze_graph)
    create_paths(columns, rows, maze_graph)
    minimum_spanning_tree = nx.minimum_spanning_tree(maze_graph)
    maze_graph.remove_edges_from(list(set(maze_graph.edges) - set(minimum_spanning_tree.edges)))
    return maze_graph


def draw_maze(maze, start_node, end_node, path):
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

    plt.plot(start_node[0] + 0.5, start_node[1] + 0.5, 'ro', markersize=8)
    plt.plot(end_node[0] + 0.5, end_node[1] + 0.5, 'go', markersize=8)

    for i in range(len(path)-1):
        u = path[i]
        v = path[i+1]
        x1, y1 = u
        x2, y2 = v
        plt.plot([x1 + 0.5, x2 + 0.5], [y1 + 0.5, y2 + 0.5], 'r', linewidth=2)
    plt.axis('off')
    plt.savefig('trivial_maze.png')
    plt.show()


maze = generate_trivial_maze(20, 10)
start_node = (4, 5)
end_node = (13, 7)
path = nx.astar_path(maze, start_node, end_node)

draw_maze(maze, start_node, end_node, path)