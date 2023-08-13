# Importing Libraries
import random
import pygame as py
import time

# Initializing pygame
py.init()

# Window
w, h = 800, 600
window = py.display.set_mode((800, 600))
running = True
py.display.set_caption("Pong Game")

# Rackets and Ball
white = (255, 255, 255)


def draw_racket1(x1, y1, x2, y2):
    racket1 = py.draw.line(window, white, (x1, y1), (x2, y2), 12)


def draw_racket2(x1, y1, x2, y2):
    racket2 = py.draw.line(window, white, (x1, y1), (x2, y2), 12)


def draw_ball(x, y):
    py.draw.circle(window, white, (x, y), 7)


# Movement
def racket2MoveUp():
    racket2StartY += 10
    racket2EndY += 10


def racket2MoveUp():
    racket2StartY -= 10
    racket2EndY -= 10


racket1StartX, racket1StartY = 5, h // 2
racket1EndX, racket1EndY = 5, h // 2 + 50

racket2StartX, racket2StartY = 793, h // 2
racket2EndX, racket2EndY = 793, h // 2 + 50

ballX = w // 2
ballY = h // 2

ballXSpeed = 0.5
ballYSpeed = 0.5


# Collision
def isCollision():
    pass


# Game Loop
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                pass
            if event.key == py.K_UP:
                racket2MoveUp()
            if event.key == py.K_DOWN:
                racket_move_up()
    if ballX <= 0:
        ballX = 0
    if ballX >= w:
        ballX = w
    if ballY <= 0:
        ballY = 0
    if ballY >= h:
        ballY = h
    window.fill((0, 0, 0))
    draw_ball(ballX, ballY)
    draw_racket1(racket1StartX, racket1StartY, racket1EndX, racket1EndY)
    draw_racket2(racket2StartX, racket2StartY, racket2EndX, racket2EndY)
    ballX += ballXSpeed
    # time.sleep(0.5)
    py.display.update()
