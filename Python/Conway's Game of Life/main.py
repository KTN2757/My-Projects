"""Requirements."""
# Any live cell with fewer than two live neighbours dies (referred to as underpopulation).
# Any live cell with more than three live neighbours dies (referred to as overpopulation).
# Any live cell with two or three live neighbours lives, unchanged, to the next generation.
# Any dead cell with exactly three live neighbours comes to life.

import random
import time

import pygame as py

w, h = 800, 608


class Cell:
    """Cell class."""

    def __init__(self, parent_window, x, y):
        self.size = 16
        self.parent_window = parent_window
        self.x, self.y = x, y
        self.w, self.h = 16, 16

    def draw(self):
        """Draws the cell."""
        py.draw.rect(self.parent_window, (255, 255, 255),
                     (self.x, self.y, self.w, self.h))


class Game:
    """Game class."""

    def __init__(self):
        py.init()
        self.window = py.display.set_mode((w, h))
        self.clock = py.time.Clock()
        self.cell = Cell(self.window, 160, 160)

    def draw_grid(self):
        """Draws grid."""
        size = 16
        for x in range(0, w, size):
            for y in range(0, h, size):
                py.draw.rect(self.window, (0, 0, 0),
                             (x, y, size, size), 1)

    def run(self):
        """Runs the game."""
        running = True
        while running:
            self.clock.tick(60)
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False

            self.window.fill((128, 128, 128))
            self.cell.draw()
            self.draw_grid()

            py.display.update()
        py.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
