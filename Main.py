import pygame
from collections import deque
import random
from Algorithm import create_adjacent_grid, BFS, DFS_long_path
import sys

x = 40
y = 20
block_size = 30
border_size = 30
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = "green"
RED = "red"
WINDOW_HEIGHT = y*block_size
WINDOW_WIDTH = x*block_size
snake = deque([(1, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1)])
#snake = deque([(2, 2), (2, 3), (2, 4), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5),
#                  (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0),
#                     (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
#snake = deque([(2, 2), (2, 3), (2, 4), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 9)])


def main():
    global SCREEN, CLOCK
    global apple


    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    grid = create_adjacent_grid(x, y)
    all_points = list(grid.keys())
    apple = random.choice(list(set(all_points)-set(snake)))
    last_apple = None
    delay = 0

    current_path = BFS(grid, snake, apple)
    if not current_path:
        current_path = DFS_long_path(grid, snake, apple)

    while True:
        drawGrid()
        drawBorder(*snake[0])
        if not current_path:
            pygame.display.update()
            break
        next_space = current_path.pop()


        if next_space == apple:
            last_apple = apple
            snake.appendleft(apple)
            apple = random.choice(list(set(all_points)-set(snake)))
            current_path = BFS(grid, snake, apple)
            if not current_path:
                current_path = DFS_long_path(grid, snake, apple)


        else:
            snake.appendleft(next_space)

        if next_space != last_apple:
            # what happens if you collect another apple before the tail reaches
            snake.pop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        pygame.time.wait(delay)

    # Game over
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def drawGrid():
    # for i in range(len(snake)):
        # if i != 0:
        #     prev_body = snake[i-1]
        # if i != len(snake):
        #     next_body = snake[i+1]
            # node = (i, j)
            # neighbors = []

            # # Add the neighboring nodes to the list (excluding diagonals)
            # for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            #     new_x, new_y = i + dx, j + dy
            #     if 0 <= new_x < x and 0 <= new_y < y and (new_x, new_y) != node:
            #         neighbors.append((new_x, new_y))

    for x in range(0, WINDOW_WIDTH, block_size):
        for y in range(0, WINDOW_HEIGHT, block_size):

            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(SCREEN, BLACK, rect) #change to WHITE for grid

    for body_x, body_y in snake:
        body_rect = pygame.Rect(body_x*block_size, body_y*block_size, block_size, block_size)
        pygame.draw.rect(SCREEN, GREEN, body_rect)

    body_rect = pygame.Rect(apple[0]*block_size, apple[1]*block_size, block_size, block_size)
    pygame.draw.rect(SCREEN, RED, body_rect)

def drawBorder(x, y, location='top', color='blue'):
    if location == 'top':
        length = block_size
        height = border_size
        a = 0
        b = 0
    elif location == 'bottom':
        length = block_size
        height = border_size
        a = 0
        b = block_size - height
    elif location == 'left':
        length = border_size
        height = block_size
        a = 0
        b = 0
    elif location == 'right':
        length = border_size
        height = block_size
        a = block_size - height
        b = 0

    border_rect = pygame.Rect(x*block_size+a, y*block_size+b, length, height)
    pygame.draw.rect(SCREEN, color, border_rect)

main()
