from collections import deque


def BFS(G, snake, apple):
    snake_head = snake[0]

    if snake_head == apple:
        return

    Q = deque([[snake_head]])
    dist = {snake_head: 0}
    E = set()
    for node in snake:
        E.add(node)

    while Q:
        path = Q.popleft()
        v = path[-1]
        for num in G[v]:
            if num not in E:
                Q.append(path + [num])
                E.add(num)
                dist[num] = dist[v] + 1
                if num == apple:
                    if len(path) == 1:
                        return apple
                    else:
                        return path[1] #path + [num]

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


#print(grid)
(BFS(grid, [(1, 2), (1, 3), (1, 4)], (5, 2)))
