import pygame
from collections import deque
import random
from Algorithm import create_adjacent_grid, BFS, DFS_long_path
import sys

x = 40
y = 20
block_size = 30
border_size = 3
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = "green"
RED = "red"
BLUE = "blue"
WINDOW_HEIGHT = y*block_size
WINDOW_WIDTH = x*block_size
snake = deque([(1, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1), (2, 1)])
snake = deque([(2, 2), (2, 3), (2, 4), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5),
                 (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0),
                    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
# snake = deque([(2, 2), (2, 3), (2, 4), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5),
#                    (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0),
#                      (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 9)])
snake = deque([(4, 13), (4, 12), (4, 11), (4, 10), (4, 9), (3, 9), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (2, 18), (1, 18), (1, 17), (1, 16), (1, 15), (1, 14), (1, 13), (1, 12), (1, 11), (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18), (0, 19), (1, 19), (2, 19), (3, 19), (4, 19), (5, 19), (6, 19), (7, 19), (8, 19), (9, 19), (10, 19), (11, 19), (12, 19), (13, 19), (14, 19), (15, 19), (16, 19), (17, 19), (18, 19), (19, 19), (20, 19), (21, 19), (22, 19), (23, 19), (24, 19), (25, 19), (26, 19), (27, 19), (28, 19), (29, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19), (30, 19)])


def main():
    global SCREEN, CLOCK
    global apple

    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    grid = create_adjacent_grid(x, y)
    all_points = list(grid.keys())
    font = pygame.font.Font(None, 75)
    apple = random.choice(list(set(all_points)-set(snake)))
    delay = 10

    current_path = BFS(grid, snake, apple)
    if not current_path:
        current_path = DFS_long_path(grid, snake, apple)
        print(current_path)

    while True:
        drawGrid()
        # drawBorder(*snake[0], 'bottom')
        # drawBorder(*snake[0], 'left')
        # drawBorder(*snake[0], 'right')
        if not current_path:
            text = font.render(str(len(snake)), True, "blue")
            text_rect = text.get_rect()
            text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            SCREEN.blit(text, text_rect)
            pygame.display.update()
            break
        next_space = current_path.pop()


        if next_space == apple:
            snake.appendleft(apple)
            apple = random.choice(list(set(all_points)-set(snake)))
            current_path = BFS(grid, snake, apple)
            if not current_path:
                current_path = DFS_long_path(grid, snake, apple)
                # print(current_path)

        else:
            snake.appendleft(next_space)
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

    for x in range(0, WINDOW_WIDTH, block_size):
        for y in range(0, WINDOW_HEIGHT, block_size):

            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(SCREEN, BLACK, rect) # change to WHITE for grid

    # draw snake
    for body_x, body_y in snake:
        body_rect = pygame.Rect(body_x*block_size, body_y*block_size, block_size, block_size)
        pygame.draw.rect(SCREEN, GREEN, body_rect)

    # draw apple
    body_rect = pygame.Rect(apple[0]*block_size, apple[1]*block_size, block_size, block_size)
    pygame.draw.rect(SCREEN, RED, body_rect)

    # color snake head
    body_rect = pygame.Rect(snake[0][0]*block_size, snake[0][1]*block_size, block_size, block_size)
    pygame.draw.rect(SCREEN, BLUE, body_rect)

    # draw snake borders
    for i in range(len(snake)):
        body_x, body_y = snake[i]
        prev_body = None
        next_body = None
        if i != 0:
            prev_body = snake[i-1]
        if i != len(snake) - 1:
            next_body = snake[i+1]

        if (body_x, body_y - 1) != prev_body and (body_x, body_y - 1) != next_body:
            drawBorder(body_x, body_y, 'top')
        if (body_x - 1, body_y) != prev_body and (body_x - 1, body_y) != next_body:
            drawBorder(body_x, body_y, 'left')
        if (body_x, body_y + 1) != prev_body and (body_x, body_y + 1) != next_body:
            drawBorder(body_x, body_y, 'bottom')
        if (body_x + 1, body_y) != prev_body and (body_x + 1, body_y) != next_body:
            drawBorder(body_x, body_y, 'right')

def drawBorder(x, y, location='top', color='black'):
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
        a = block_size - length
        b = 0

    border_rect = pygame.Rect(x*block_size+a, y*block_size+b, length, height)
    pygame.draw.rect(SCREEN, color, border_rect)

main()
