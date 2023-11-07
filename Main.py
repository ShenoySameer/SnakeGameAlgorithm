import pygame


x = 40
y = 20
blocksize = 30
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = "green"
RED = "red"
WINDOW_HEIGHT = y*blocksize
WINDOW_WIDTH = x*blocksize
snake = [(1, 2), (1, 3), (1, 4)]
apple = (5,2)

apple = (10, 10)
def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():
    for x in range(0, WINDOW_WIDTH, blocksize):
        for y in range(0, WINDOW_HEIGHT, blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1) #change to WHITE for grid

    for body_x, body_y in snake:
        body_rect = pygame.Rect(body_x*blocksize, body_y*blocksize, blocksize, blocksize)
        pygame.draw.rect(SCREEN, GREEN, body_rect)

    body_rect = pygame.Rect(apple[0]*blocksize, apple[1]*blocksize, blocksize, blocksize)
    pygame.draw.rect(SCREEN, RED, body_rect)

main()

