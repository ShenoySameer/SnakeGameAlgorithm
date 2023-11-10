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

def BFS_path(G, snake, apple):
    snake_head = snake[0]

    if snake_head == apple:
        return 0, []

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
                    new_snake = new_path[::-1] + [snake[i+1] for i in range(len(snake)-len(new_path))]
                    accessible_nodes = BFS_basic(G, new_snake)
                    score = len(accessible_nodes - set(new_snake)) / (len(G.keys() - set(new_snake)))
                    return score, new_path[:0:-1]
    
    return 0, []

# Provides the snake with a longer path until it can find a safe shortest path
# If there is no safe one, return the safest option
# If there is no way to survivie, return the longest path
def DFS_long_path(G, snake, apple):
    snake_head = snake[0]

    Q = [[snake_head]]
    E = set()
    longest_path = [snake_head]
    escape_paths = []

    accessible_nodes = BFS_basic(G, snake)
    target = snake_head
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
        adj_nodes.sort(key = lambda x: travel_distance(x, target))
        for node in adj_nodes:
            new_path = path + [node]
            new_snake = new_path[::-1] + [snake[i+1] for i in range(len(snake)-len(new_path))]
            # Add snake to explored
            if node not in (E | set(new_snake[1:])):
                Q.append(new_path)
                # Find out if at any point the snake could reach the target point
                # as the tail leaves that point
                if travel_distance(node, target) >= dist_from_tail - len(new_path):
                    score, escape_path = BFS_path(G, new_snake, apple)
                    if score >= 0.8:
                        return escape_path + new_path[:0:-1]
                    elif score > 0:
                        escape_paths.append((score, escape_path + new_path[:0:-1]))
                longest_path = max(longest_path, new_path, key=len)

    if escape_paths:
        return max(escape_paths)[1]
    
    new_snake = longest_path[::-1] + [snake[i+1] for i in range(len(snake)-len(longest_path))]
    return BFS_path(G, new_snake, apple)[1] + longest_path[:0:-1]


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

