# Importing Libraries
import random
import pygame as py

# Initializing pygame
py.init()

# Window
w, h = 800, 600
window = py.display.set_mode((800, 600))
running = True
py.display.set_caption("Pong Game")
window.fill((0, 0, 0))

line1 = py.draw.line(window, (255, 255, 255), (5, h//2), (5, h//2+50), 12)
line2 = py.draw.line(window, (255, 255, 255), (793, h//2), (793, h//2+50), 12)

# Game Loop
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    py.display.update()
