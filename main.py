import pygame
import random
from pygame import font

#Initializing modules iof pygame
pygame.init()

#Setting display which is the window screen
SCREEN = pygame.display.set_mode((500, 750))

#Setting Background
BACKGROUND_IMAGE = pygame.image.load('background1.png')

# Player
PLAYER_IMAGE = pygame.image.load("player1.png")
player_x = 50
player_y = 300
player_y_change = 0


def display_player(x, y):
    SCREEN.blit(PLAYER_IMAGE, (x, y))


#Adding obstacles
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150, 450)
OBSTACLE_COLOR = (255, 255, 255)
OBSTACLE_X_CHANGE = -4
obstacle_x = 500


def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_obstacle_height = (635 - height - 100)
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 635, OBSTACLE_WIDTH, bottom_obstacle_height))


#Detecting collision
def collision_detection(obstacle_x, obstacle_height, player_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50+64):
        if (player_y <= obstacle_height) or (player_y >= (bottom_obstacle_height + 64)):
            return True
    else:
        return False


score = 0
SCORE_FONT = pygame.font.Font('FreeSansBold.ttf', 32)


def score_display(score):
    display = SCORE_FONT.render(f"Score: {score}", True, (30, 30, 30))
    SCREEN.blit(display, (10, 10))

running = True
while running:

    SCREEN.fill((0, 0, 0))

    #Display background image
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #When pressing exit user quits program
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_y_change = -6

        if event.type == pygame.KEYUP:
            player_y_change = 3

    player_y += player_y_change

    if player_y <= 0:
        player_y = 0
    if player_y >= 571:
        player_y = 571

    obstacle_x += OBSTACLE_X_CHANGE
    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(200, 400)
        score += 1
    display_obstacle(OBSTACLE_HEIGHT)

    #Collision
    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, player_y, (OBSTACLE_HEIGHT + 150))

    if collision:
        pygame.quit()

    display_player(player_x, player_y)

    #Display score
    score_display(score)
    #Update display whenever user starts
    pygame.display.update()

#Quit game
pygame.quit()