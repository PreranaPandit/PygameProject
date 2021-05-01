import pygame

# initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# title and icon
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('project.png')
pygame.display.set_icon(icon)

# Adding player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480

def player():
    #blit --> draw
    screen.blit(playerImg, (playerX,playerY))

# Game loop
running = True

while running:

    # RGB COLOR TO RGB for background color
    screen.fill((58, 0, 28))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player()

        pygame.display.update()

