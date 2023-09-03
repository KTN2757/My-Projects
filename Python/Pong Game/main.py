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

# Rackets and Ball
white = (255, 255, 255)


def draw_racket1(x1, y1):
    global racket1
    racket1 = py.draw.rect(window, white, (x1, y1, 10, 50))


def draw_racket2(x1, y1):
    global racket2
    racket2 = py.draw.rect(window, white, (x1, y1, 10, 50))


def draw_ball(x, y):
    global ball
    ball = py.draw.circle(window, white, (x, y), 7)


# Movement & Animation
racket1X, racket1Y = 5, h // 2

racket2X, racket2Y = 785, h // 2

ballX = w // 2
ballY = h // 2

ballXSpeed = 0.5
ballYSpeed = 0.5


def racket2MoveUp(x1, y1):
    racket2Y = 2000
    print(racket2Y)
    return y1


def racket2MoveDown():
    racket2StartY -= 10
    racket2EndY -= 10


def ballAnimation():
    global ballXSpeed, ballYSpeed
    if ballX <= 0 or ballX >= w:
        ballXSpeed *= -1
    if ballY <= 0 or ballY >= h:
        ballYSpeed *= -1


# Vectors
# racket1Vector = [racket1EndX - racket1StartX, racket1EndY - racket1EndY]
# racket2Vector = [racket2EndX - racket2StartX, racket2EndY - racket2EndY]
# np.array(racket1Vector)
# np.array(racket2Vector)


# Collision
def isCollidedWith(self, racket1):
    return self.rect.colliderect(racket1.rect)


# Game Over


# Game Loop
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                pass
            if event.key == py.K_UP:
                racket2MoveUp(racket2X, racket2Y)
            if event.key == py.K_DOWN:
                pass
    if ball.isCollidedWith(racket1):
        print("asdadi")

    window.fill((0, 0, 0))
    draw_ball(ballX, ballY)
    draw_racket1(racket1X, racket1Y)
    draw_racket2(racket2X, racket2Y)
    ballAnimation()
    ballX += ballXSpeed
    ballY += ballYSpeed
    # time.sleep(0.5)
    py.display.update()
