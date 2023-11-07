def dfs_80(graph, snake, apple):
    E = {}
    for node in snake:
        E.add(node)


def create_adjacent_grid(x, y):
    grid = {}
    for i in range(x):
        for j in range(y):
            node = (i, j)
            neighbors = []

            # Add the neighboring nodes to the list (excluding diagonals)
            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < x and 0 <= new_y < y and (new_x, new_y) != node:
                    neighbors.append((new_x, new_y))

            grid[node] = neighbors

    return grid

x = 10  # Width of the grid
y = 10  # Height of the grid
grid = create_adjacent_grid(x, y)
for node, neighbors in grid.items():
    print(f"Node {node} is connected to: {neighbors}")



