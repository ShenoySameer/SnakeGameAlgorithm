import pygame
from collections import deque
import random
from Algorithm import create_adjacent_grid, BFS_path, DFS_long_path
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
snake = deque([(2, 1), (1, 1)])


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

    score, current_path = BFS_path(grid, snake, apple)
    if score < 0.8:
        current_path = DFS_long_path(grid, snake, apple)

    while True:
        drawGrid()
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
            score, current_path = BFS_path(grid, snake, apple)
            if score < 0.8:
                current_path = DFS_long_path(grid, snake, apple)
                

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
