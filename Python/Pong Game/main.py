# Importing Libraries
import random
import pygame as py
import time
import numpy as np

# Initializing pygame
py.init()

# Window
w, h = 800, 600
window = py.display.set_mode((800, 600))
running = True
py.display.set_caption("Pong Game")
gameOverFont = py.font.SysFont("Comic Sans MS.ttf", 64)
restartFont = py.font.SysFont("Comic Sans MS.ttf", 32)

# Rackets and Ball
white = (255, 255, 255)


def draw_racket1(x1, y1, x2, y2):
    global racket1
    racket1 = py.draw.rect(window, white, (x1, y1, x2, y2))


def draw_racket2(x1, y1, x2, y2):
    global racket2
    racket2 = py.draw.rect(window, white, (x1, y1, x2, y2))


def draw_ball(x, y):
    global ball
    ball = py.draw.circle(window, white, (x, y), 7)


# Movement & Animation
racket1X1, racket1Y1 = 5, h // 2
racket1X2, racket1Y2 = 10, 50

racket2X1, racket2Y1 = 785, h // 2
racket2X2, racket2Y2 = 10, 50

ballX = w // 2
ballY = h // 2

ballXSpeed = 0
ballYSpeed = 0


def racket2MoveUp(x1, y1, x2, y2):
    pass


def racket2MoveDown():
    racket2StartY -= 10
    racket2EndY -= 10


# Collision


# Game Over
gameIsOver = False


def gameOver(x, y):
    x = 1000
    y = 1000
    text = gameOverFont.render("GAME OVER", True, (255, 255, 255))
    window.blit(text, (w // 2 - 150, h // 2))
    text2 = restartFont.render(
        "Press 'r' to restart or 'q' to quit.", True, (255, 255, 255)
    )
    window.blit(text2, (w // 2 - 175, h // 2 + 50))


# Game Loop
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                pass
            if event.key == py.K_UP:
                racket2MoveUp(racket2X1, racket2Y1, racket2X2, racket2Y2)
            if event.key == py.K_DOWN:
                pass
            if gameIsOver == True and event.key == py.K_r:
                ballX = w // 2
                ballY = h // 2
            if gameIsOver == True and event.key == py.K_q:
                running = False

    window.fill((0, 0, 0))
    draw_ball(ballX, ballY)
    draw_racket1(racket1X1, racket1Y1, racket1X2, racket1Y2)
    draw_racket2(racket2X1, racket2Y1, racket2X2, racket2Y2)
    ballX += ballXSpeed
    ballY += ballYSpeed
    if ballX <= 0 or ballX >= w or ballY <= 0 or ballY >= h:
        gameOver(ballX, ballY)
        gameIsOver = True
    # time.sleep(0.5)
    py.display.update()
