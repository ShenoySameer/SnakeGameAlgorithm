from collections import deque
from math import sqrt

def BFS_basic(G, snake):
    snake_head = snake[0]

    Q = deque([snake_head])
    depth = {snake_head: 0}
    E = set()
    snake_set = set(snake)

    while Q:
        v = Q.popleft()
        if depth[v]+1 <= len(snake):
            if snake[-(depth[v]+1)] in E:
                E.remove(snake[-(depth[v]+1)])
        for node in G[v]:
            if node not in E:
                E.add(node)
                depth[node] = depth[v] + 1
                if node not in snake_set:
                    Q.append(node)
    return E

def BFS(G, snake, apple):
    snake_head = snake[0]

    if snake_head == apple:
        return

    resort = []
    Q = deque([[snake_head]])
    E = set(snake)

    while Q:
        path = Q.popleft()
        v = path[-1]

        if len(path) <= len(snake):
            if snake[-len(path)] in E:
                E.remove(snake[-len(path)])
        
        for node in G[v]:
            new_path = path + [node]
            if node not in E:
                Q.append(new_path)
                E.add(node)
                if node == apple:
                    score = len(BFS_basic(G, new_path[::-1])) / (len(G))
                    print(score)
                    if score > 0.8:
                        return new_path[:0:-1]
                    else:
                        resort.append((score, new_path[:0:-1]))

    # resort.sort(reverse=True)
    # print(resort)
    # return resort[0]
    return []


def DFS_long_path(G, snake, apple):
    snake_head = snake[0]

    Q = [[snake_head]]
    depth = {snake_head: 0}
    E = set(snake)
    longest_path = []
    
    accessible_nodes = BFS_basic(G, snake)
    for i in range(len(snake)):
        body = snake[len(snake) - (i+1)]
        if body in accessible_nodes:
            target = body
            dist_from_tail = i
            break

    while Q:
        path = Q.pop()
        v = path[-1]
        E.add(v)
        adj_nodes = G[v]
        adj_nodes.sort(key = lambda x: absolute_distance(x, target))
        for node in adj_nodes:
            new_path = path + [node]
            if node not in E:
                # E.add(node)
                Q.append(new_path)
                depth[node] = depth[v] + 1
                # Find out if at any point the snake could reach the target point
                # as the tail leaves that point
                if travel_distance(node, target) == dist_from_tail - depth[node]:
                    new_snake = new_path[:0:-1] + [snake[i] for i in range(len(snake)-depth[node])]
                    return BFS(G, new_snake, apple) + new_path[:0:-1]
                # print(new_path)
                longest_path = max(longest_path, new_path, key=len)
            # else:
                # print(node)
    
    return longest_path[:0:-1]


def absolute_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def travel_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

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
# print(BFS(grid, [(1, 2), (1, 3), (1, 4)], (5, 2)))
snake = deque([(2, 2), (2, 3), (2, 4), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), 
                   (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0),
                     (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 9)])
print(BFS_basic(grid, snake))
print(BFS(grid, snake, (9, 9)))
print(DFS_long_path(grid, snake, (9, 9)))

# [(1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (3, 2)]

