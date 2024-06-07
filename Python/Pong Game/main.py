# Importing Libraries
"""Requirements"""

import math
import time
import pygame as py

# Window
w, h = 800, 608


class Racket:
    """Racket class."""

    def __init__(self, parent_window, x1, y1, width, height, ball):
        self.parent_window = parent_window
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.color = (255, 255, 255)
        self.ball = ball

    def draw(self):
        """Draws a racket."""
        py.draw.rect(
            self.parent_window, self.color, (self.x1, self.y1, self.width, self.height)
        )

    def move_up(self):
        """Moves the racket up."""
        if self.y1 > 0:
            self.y1 -= 0.5

    def move_down(self):
        """Moves the racket down."""
        if self.y1 < h - self.height:
            self.y1 += 0.5

    def computer_movement(self):
        """Moves the computer racket."""
        if self.y1 < self.ball.y:
            self.move_up()
        elif self.y1 > self.ball.y:
            self.move_down()


class Ball:
    """Ball class."""

    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.x = w // 2
        self.y = h // 2
        self.color = (255, 255, 255)
        self.x_speed = 0.3
        self.y_speed = 0.3

    def draw(self):
        """Draws the ball."""
        py.draw.circle(self.parent_window, self.color, (self.x, self.y), 7)

    def move(self):
        """Moves the ball."""
        self.x += self.x_speed
        self.y += self.y_speed


class Game:
    """Main game."""

    def __init__(self):
        py.init()
        self.window = py.display.set_mode((w, h))
        py.display.set_caption("Pong Game")
        self.is_game_over = False
        self.ball = Ball(self.window)

        racket1_x1, racket1_y1 = 5, 288
        racket1_w, racket1_h = 10, 75

        racket2_x1, racket2_y1 = 785, 288
        racket2_w, racket2_h = 10, 75

        self.racket1 = Racket(
            self.window, racket1_x1, racket1_y1, racket1_w, racket1_h, self.ball
        )
        self.racket2 = Racket(
            self.window, racket2_x1, racket2_y1, racket2_w, racket2_h, self.ball
        )

    # Collisions
    def border_collision(self):
        """Checks for border collision."""
        if self.ball.y < 0 or self.ball.y > h:
            self.ball.y_speed *= -1
        if self.ball.x < 0 or self.ball.x > w:
            self.is_game_over = self.game_over()

    def racket_collision(self):
        """Checks for racket collision."""
        if (
            self.ball.x < self.racket1.x1 + self.racket1.width
            and self.ball.y > self.racket1.y1
            and self.ball.y < self.racket1.y1 + self.racket1.height
        ):
            self.ball.x_speed *= -1
        if (
            self.ball.x > self.racket2.x1
            and self.ball.y > self.racket2.y1
            and self.ball.y < self.racket2.y1 + self.racket2.height
        ):
            self.ball.x_speed *= -1

    def restart(self):
        """Restarts the game."""
        self.ball.x, self.ball.y = w // 2, h // 2
        self.ball.x_speed, self.ball.y_speed = 0.3, 0.3
        self.racket1.x1, self.racket1.y1 = 5, 288
        self.racket1.width, self.racket1.height = 10, 50
        self.racket2.x1, self.racket2.y1 = 785, 288
        self.racket2.width, self.racket2.height = 10, 50
        self.is_game_over = False

    def game_over(self):
        """Displays \"GAME OVER\"."""
        self.is_game_over = True
        self.ball.x = 1000
        self.ball.x_speed, self.ball.y_speed = 0, 0
        self.racket1.x1, self.racket2.x1 = -500, -500
        game_over_font = py.font.SysFont("Comic Sans MS.ttf", 64)
        restart_font = py.font.SysFont("Comic Sans MS.ttf", 32)
        game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
        restart_text = restart_font.render(
            "Press 'r' to restart or 'q' to quit.", True, (255, 255, 255)
        )
        self.window.blit(game_over_text, (w // 2 - 150, 288))
        self.window.blit(restart_text, (w // 2 - 175, 330))
        return True

    def run(self):
        """Runs the game."""
        running = True
        # Game Loop
        while running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                if event.type == py.KEYDOWN:
                    if self.is_game_over:
                        if event.key == py.K_r:
                            self.restart()
                        if event.key == py.K_q:
                            running = False

            # Color
            self.window.fill((0, 0, 0))

            # Racket Control
            keys = py.key.get_pressed()
            if keys[py.K_UP]:
                self.racket2.move_up()
            if keys[py.K_DOWN]:
                self.racket2.move_down()

            # Drawing & Movement
            self.ball.draw()
            self.ball.move()
            self.racket1.draw()
            self.racket2.draw()
            self.racket1.computer_movement()

            # Check Collision & Boundary
            self.border_collision()
            self.racket_collision()
            py.display.update()


# Running the game
if __name__ == "__main__":
    game = Game()
    game.run()
