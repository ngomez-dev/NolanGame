import pygame
import random
import time


#powerups



pygame.init()

font = pygame.font.SysFont("Arial", 32)



# Setup and Images
Heart1 = pygame.image.load('Heart1.png')
Heart1 = pygame.transform.scale(Heart1, (Heart1.get_width()*.2, Heart1.get_height()*.2))
Heart2 = pygame.image.load('Heart1.png')
Heart2 = pygame.transform.scale(Heart2, (Heart2.get_width()*.2, Heart2.get_height()*.2))
Heart3 = pygame.image.load('Heart1.png')
Heart3 = pygame.transform.scale(Heart3, (Heart3.get_width()*.2, Heart3.get_height()*.2))
Heart4 = pygame.image.load('Heart1.png')
Heart4 = pygame.transform.scale(Heart4, (Heart4.get_width()*.2, Heart4.get_height()*.2))


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
ball = pygame.Rect(390, 300, 35, 35)
ball_x_speed = 5
ball_y_speed = -5

#fireball
fireball = pygame.Rect(400, 400, 20, 20)
fireball_x_speed = 4
fireball_y_speed = -4


# Bricks
bricks = []
for i in range(5):
    for j in range(10):
        brick = pygame.Rect(j * 80 + 5, i * 30 + 5, 70, 20)
        bricks.append(brick)

# Variables
score = 0
lives = 4
level = 1
platform_speed = 6
running = True
start_time = 0
speed_multiplier = 1

#Randomize colors
brick_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
platform_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Game Loop
while running:


    text_surface = font.render("Score: "+str(score) , True, (255, 255, 255))
    Game_Over = font.render("Game Over" , True, (255, 255, 255))

#Events/Keys

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Holding Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        platform.x = platform.x - (platform_speed * speed_multiplier)
    if keys[pygame.K_RIGHT]:
        platform.x = platform.x + (platform_speed * speed_multiplier)

# Ball Movement
    ball.x = ball.x + (ball_x_speed * speed_multiplier)
    ball.y = ball.y + (ball_y_speed * speed_multiplier)

    #Powerups
    fireball.x = fireball.x + fireball_x_speed
    fireball.y = fireball.y + fireball_y_speed

    if fireball.colliderect(platform):
        fireball_y_speed = -fireball_y_speed

    if ball.colliderect(fireball):
        fireball.x = -1000
        start_time = 600
        speed_multiplier = 1.5


    if start_time > 0:
        start_time = start_time - 1
    if start_time == 0:
        speed_multiplier = 1


    screen.fill(BLACK)

# Drawings
    pygame.draw.rect(screen, platform_color, platform)
    pygame.draw.ellipse(screen, WHITE, ball)
    screen.blit(text_surface,(350, 300))
    pygame.draw.ellipse(screen,RED, fireball)
    for brick in bricks:
        pygame.draw.rect(screen,(brick_color), brick)

#Hearts
    if lives >= 1:
        screen.blit(Heart1, (WIDTH-60, HEIGHT-100))
    if lives >= 2:
        screen.blit(Heart2, (WIDTH-110, HEIGHT-100))
    if lives >= 3:
        screen.blit(Heart3, (WIDTH-160, HEIGHT-100))
    if lives >= 4:
        screen.blit(Heart4, (WIDTH-210, HEIGHT-100))


    if fireball.left <= 0 or fireball.right >= WIDTH:
        fireball_x_speed = -fireball_x_speed
    if fireball.top <= 0:
        fireball_y_speed = -fireball_y_speed
    if fireball.bottom >= HEIGHT:
        fireball_y_speed = -fireball_y_speed

    if fireball.colliderect(platform):
        fireball_y_speed = -fireball_y_speed
    for brick in bricks:
        if fireball.colliderect(brick):
            if fireball.top <= brick.bottom and fireball_y_speed < 0:
                fireball_y_speed = -fireball_y_speed
            elif fireball.bottom >= brick.top and fireball_y_speed > 0:
                fireball_y_speed = -fireball_y_speed
            else:
                fireball_x_speed = -fireball_x_speed





# Ball Colliding with Platform
    if ball.colliderect(platform):
        ball_y_speed=-ball_y_speed


 # Colliding with Bricks
    for brick in bricks:
        if ball.colliderect(brick):

#if the top of the ball is colliding with the bottom of the brick
            if ball.top <= brick.bottom and ball_y_speed < 0:
                #change the speed
                ball_y_speed = -ball_y_speed
#Bottom of ball colliding with top of brick
            elif ball.bottom >= brick.top and ball_y_speed > 0:
                ball_y_speed = -ball_y_speed
            else:
                ball_x_speed = -ball_x_speed

            score = score + 10
            bricks.remove(brick)
# Colliding off left and right walls and top.
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_x_speed = -ball_x_speed
    if ball.top <= 0:
        ball_y_speed = -ball_y_speed

# Continous Level System
    if len(bricks) == 0:
        level = level + 1
        ball.x, ball.y = 390,300
        start_time = 0
        speed_multiplier = 1
        ball_y_speed = (-1) * abs(ball_y_speed)
        ball_y_speed = ball_y_speed - 2
        fireball.x, fireball.y = 400,400
        fireball_x_speed = 4
        fireball_y_speed = -4


        # Spawn Bricks
        bricks = []
        for i in range(5):
            for j in range(10):
                brick = pygame.Rect(j * 80 + 5, i * 30 + 5, 70, 20)
                bricks.append(brick)
        platform_speed += 2
#Randomize colors every level
        brick_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        platform_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))




# Fail Condition


    if ball.top > HEIGHT:
        lives = lives - 1
        if lives > 0:
            ball.x, ball.y = 390, 300
            ball_y_speed = -5 - level

# Game Over
        else:

            screen.blit(Game_Over,(350,330))
            pygame.display.update()
            pygame.time.wait(1000)
            print("Game Over, Score:", score)
            running = False


    pygame.display.update()
    clock.tick(60)




pygame.quit()
