"""Requirements."""
# Any live cell with fewer than two live neighbours dies (referred to as underpopulation).
# Any live cell with more than three live neighbours dies (referred to as overpopulation).
# Any live cell with two or three live neighbours lives, unchanged, to the next generation.
# Any dead cell with exactly three live neighbours comes to life.

import random
import time
import pygame as py

import Input_box

w, h = 800, 608
cells = []


class Cell:
    """Cell class."""

    def __init__(self, parent_window, x, y):
        self.parent_window = parent_window
        self.x, self.y = x, y
        self.w, self.h = 32, 32
        self.color = (255, 255, 255)
        cells.append((x, y))

    def draw(self):
        """Draws the cell."""
        py.draw.rect(self.parent_window, (self.color),
                     (self.x, self.y, self.w, self.h))

    def check_neighbours(self):
        """Checks the neighbours of the cell."""
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if (
                    self.x + i * 32 >= 0
                    and self.x + i * 32 < w
                    and self.y + j * 32 >= 0
                    and self.y + j * 32 < h
                ):
                    if self.parent_window.get_at(
                        (self.x + i * 32, self.y + j * 32)
                    ) == (
                        255,
                        255,
                        255,
                    ):
                        neighbours.append((self.x + i * 32, self.y + j * 32))
        if len(neighbours) < 2:
            self.color = (128, 128, 128)
        if len(neighbours) > 3:
            self.color = (128, 128, 128)
        if len(neighbours) == 3:
            self.color = (255, 255, 255)
        return neighbours


class Game:
    """Game class."""

    def __init__(self):
        py.init()
        self.window = py.display.set_mode((w, h))
        self.clock = py.time.Clock()
        self.window.fill((128, 128, 128))

    def draw_grid(self):
        """Draws grid."""
        size = 32
        for x in range(0, w, size):
            for y in range(0, h, size):
                py.draw.rect(self.window, (0, 0, 0), (x, y, size, size), 1)

    def add_cell(self, x, y):
        """Adds a new cell."""
        return Cell(self.window, x, y)

    def run(self):
        """Runs the game."""
        running = True
        while running:
            self.clock.tick(60)
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False

                if event.type == py.KEYDOWN:
                    if event.key == py.K_UP:
                        Input_box.run()
                        cell = self.add_cell(
                            random.randint(0, w - 32) // 32 * 32,
                            random.randint(0, h - 32) // 32 * 32,
                        )
                        cell.draw()
                        print(cells)

            # print(self.cell.check_neighbours())
            self.draw_grid()

            py.display.update()
        py.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
