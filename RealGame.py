import pygame

# Make direction change only for the bottom of Bricks
# make it bounce of the top



pygame.init()

hearts = pygame.image.load('3hearts.png')



# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 120)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
CYAN = (9, 221, 232)

# Platform
platform = pygame.Rect(350, 550, 100, 10)


# Ball
ball = pygame.Rect(390, 300, 20, 20)
ball_x_speed = 4
ball_y_speed = -4


# Bricks
bricks = []
for i in range(5):
    for j in range(10):
        brick = pygame.Rect(j * 80 + 5, i * 30 + 5, 70, 20)
        bricks.append(brick)


score = 0
lives = 3
level = 1
running = True

while running:

#Events/Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        platform.x = platform.x - 6
    if keys[pygame.K_RIGHT]:
        platform.x = platform.x + 6
# Ball Movement
    ball.x = ball.x + ball_x_speed
    ball.y = ball.y + ball_y_speed



    screen.fill(BLACK)

# Drawings
    pygame.draw.rect(screen, CYAN, platform)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick in bricks:
        pygame.draw.rect(screen,(RED), brick)
    # screen.blit(hearts, ())







    pygame.display.update()
    clock.tick(60)

# Ball Colliding
    if ball.colliderect(platform):
        ball_y_speed=-ball_y_speed



    for brick in bricks:
        if ball.colliderect(brick):
            ball_y_speed = -ball_y_speed
            score = score + 10
            bricks.remove(brick)

    if ball.left <= 0 or ball.right >= WIDTH:
        ball_x_speed = -ball_x_speed
    if ball.top >= HEIGHT:
        ball_y_speed = -ball_y_speed


# Fail Condition


    if ball.bottom >= HEIGHT:
        lives = lives - 1
        if lives > 0:
            ball.x, ball.y = 390, 300
            ball_y_speed = -4
        else:
            print("Game Over, Score:", score)
            running = False







pygame.quit()
