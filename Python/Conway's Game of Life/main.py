"""Requirements."""
# Any live cell with fewer than two live neighbours dies (referred to as underpopulation).
# Any live cell with more than three live neighbours dies (referred to as overpopulation).
# Any live cell with two or three live neighbours lives, unchanged, to the next generation.
# Any dead cell with exactly three live neighbours comes to life.

import random
import pygame as py

w, h = 800, 608
CELL_SIZE = 32


class Game:
    """Game class."""

    def __init__(self):
        py.init()
        self.window = py.display.set_mode((w, h))
        py.display.set_caption("Conway's Game of Life")
        self.clock = py.time.Clock()
        # How many cells are there x-wise and y-wise
        self.grid_xcount = w // CELL_SIZE
        self.grid_ycount = h // CELL_SIZE

        # Just a 2D array with a bunch of 0s
        self.grid = [
            [0 for _ in range(self.grid_xcount)] for _ in range(self.grid_ycount)
        ]
        self.randomize_grid()
        self.paused = True

    def draw_grid(self):
        """Draws grid."""
        self.window.fill((128, 128, 128))
        for row in range(self.grid_ycount):
            for col in range(self.grid_xcount):
                x = col * CELL_SIZE
                y = row * CELL_SIZE

                if self.grid[row][col] == 1:
                    py.draw.rect(
                        self.window, (255, 255, 255), (x, y, CELL_SIZE, CELL_SIZE)
                    )

                py.draw.rect(self.window, (60, 60, 60), (x, y, CELL_SIZE, CELL_SIZE), 1)
        font = py.font.Font(None, 24)
        instructions = [
            "SPACE: Play/Pause",
            "R: Randomize",
            "C: Clear",
            "Click: Toggle cell",
            "Q: Quit",
        ]

        for i, text in enumerate(instructions):
            color = (0, 255, 0) if not self.paused else (255, 100, 100)
            surf = font.render(text, True, color)
            self.window.blit(surf, (10, 10 + i * 25))

    def update_grid(self):
        """Update grid according to Game of Life rules."""
        new_grid = [
            [0 for _ in range(self.grid_xcount)] for _ in range(self.grid_ycount)
        ]

        for row in range(self.grid_ycount):
            for col in range(self.grid_xcount):
                neighbours = self.count_neighbours(row, col)
                current = self.grid[row][col]

                if current == 1:
                    if neighbours < 2:
                        new_grid[row][col] = 0
                    elif neighbours > 3:
                        new_grid[row][col] = 0
                    else:
                        new_grid[row][col] = 1
                else:
                    if neighbours == 3:
                        new_grid[row][col] = 1

        self.grid = new_grid

    def clear_grid(self):
        """Clear all cells."""
        self.grid = [
            [0 for _ in range(self.grid_xcount)] for _ in range(self.grid_ycount)
        ]

    def randomize_grid(self):
        """Fill grid with random living cells."""
        for row in range(self.grid_ycount):
            for col in range(self.grid_xcount):
                self.grid[row][col] = random.choice([0, 0, 0, 1])

    def count_neighbours(self, row, col):
        """Count living neighbours around a cell."""
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue

                new_row = row + i
                new_col = col + j

                if 0 <= new_row < self.grid_ycount and 0 <= new_col < self.grid_xcount:
                    count += self.grid[new_row][new_col]

        return count

    def handle_click(self, pos):
        """Toggle cell on mouse click."""
        x, y = pos
        col = x // CELL_SIZE
        row = y // CELL_SIZE

        if 0 <= row < self.grid_ycount and 0 <= col < self.grid_xcount:
            self.grid[row][col] = 1 - self.grid[row][col]

    def run(self):
        """Main game loop."""
        running = True

        while running:
            self.clock.tick(10)

            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False

                if event.type == py.KEYDOWN:
                    if event.key == py.K_SPACE:
                        self.paused = not self.paused
                    elif event.key == py.K_r:
                        self.randomize_grid()
                    elif event.key == py.K_c:
                        self.clear_grid()
                    elif event.key == py.K_q:
                        running = False

                if event.type == py.MOUSEBUTTONDOWN:
                    self.handle_click(py.mouse.get_pos())

            if not self.paused:
                self.update_grid()

            self.draw_grid()
            py.display.update()

        py.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
