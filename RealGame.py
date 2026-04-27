import pygame


pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Platform
platform = pygame.Rect(350, 550, 100, 10)

# Ball
ball = pygame.Rect(390, 300, 20, 20)


# Bricks
bricks = []
for i in range(5):  # rows
    for j in range(10):  # columns
        brick = pygame.Rect(j * 80 + 5, i * 30 + 5, 70, 20)
        bricks.append(brick)


score = 0
running = True

while running:
    screen.fill(BLACK)


    pygame.draw.rect(screen, BLUE, platform)
    pygame.draw.ellipse(screen, WHITE, ball)





    pygame.display.update()
    clock.tick(60)

pygame.quit()
