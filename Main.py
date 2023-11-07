import pygame
from collections import deque
import random
from Algorithm import create_adjacent_grid, BFS
import sys

x = 40
y = 20
blocksize = 30
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = "green"
RED = "red"
WINDOW_HEIGHT = y*blocksize
WINDOW_WIDTH = x*blocksize
snake = deque([(1, 1), (1, 2)])


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
    delay = 100

    while True:
        drawGrid()
        next_space = BFS(grid, snake, apple)
        if next_space == apple:
            last_apple = apple
            snake.appendleft(apple)
            apple = random.choice(list(set(all_points)-set(snake)))

        else:
            snake.appendleft(next_space)

        if next_space != last_apple:
            #what happens if you collect another apple before the tail reaches
            snake.pop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        pygame.time.wait(delay)

def drawGrid():
    for x in range(0, WINDOW_WIDTH, blocksize):
        for y in range(0, WINDOW_HEIGHT, blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(SCREEN, BLACK, rect) #change to WHITE for grid

    for body_x, body_y in snake:
        body_rect = pygame.Rect(body_x*blocksize, body_y*blocksize, blocksize, blocksize)
        pygame.draw.rect(SCREEN, GREEN, body_rect)

    body_rect = pygame.Rect(apple[0]*blocksize, apple[1]*blocksize, blocksize, blocksize)
    pygame.draw.rect(SCREEN, RED, body_rect)

main()

