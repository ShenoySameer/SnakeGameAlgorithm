from collections import deque

def BFS_basic(G, snake):
    snake_head = snake[0]

    Q = deque([[snake_head]])
    dist = {snake_head: 0}
    E = set()
    snake_set = set(snake)

    while Q:
        path = Q.popleft()
        v = path[-1]
        if len(path) <= len(snake):
            if snake[-len(path)] in E:
                E.remove(snake[-len(path)])
        for num in G[v]:
            if num not in E.union(snake_set):
                Q.append(path + [num])
                E.add(num)
                dist[num] = dist[v] + 1
    return E

def BFS(G, snake, apple):
    snake_head = snake[0]

    if snake_head == apple:
        return

    resort = []
    Q = deque([[snake_head]])
    dist = {snake_head: 0}
    E = set()
    for node in snake:
        E.add(node)

    while Q:
        path = Q.popleft()
        v = path[-1]
        if len(path) <= len(snake):
            if snake[-len(path)] in E:
                E.remove(snake[-len(path)])
        for num in G[v]:
            if num not in E:
                Q.append(path + [num])
                E.add(num)
                dist[num] = dist[v] + 1
                if num == apple:
                    if len(path) == 1:
                        return apple
                    else:
                        score = len(BFS_basic(G, (path[1:] + [num]))) / (len(G))
                        print(score)
                        if score > 0.8:
                            return (path[1:] + [num])[::-1]
                        else:
                            resort.append((score, (path[1:] + [num])[::-1]))

    resort.sort(reverse=True)
    print(resort)
    return resort[0]

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
