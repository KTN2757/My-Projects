import pygame
import random

# Initialize
pygame.init()
w, h = 800, 600
dvdW, dvdH = 124, 124
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("DVD Logo")
logo = pygame.image.load("dvd-logo.png")
pygame.display.set_icon(logo)

# Player
playerImg = pygame.image.load("dvd-logo.png")
playerX = random.randint(0, w - dvdW)
playerY = random.randint(0, h - dvdH)
xSpeed = 0.1
ySpeed = 0.1


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player(playerX, playerY)
    # Movement
    playerX += xSpeed
    playerY += ySpeed
    if playerX + dvdW >= w:
        xSpeed *= -1
    elif playerX <= 0:
        xSpeed *= -1
    if playerY + dvdH >= h:
        ySpeed *= -1
    elif playerY <= 0:
        ySpeed *= -1
    pygame.display.update()
