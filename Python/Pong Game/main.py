# Importing Libraries
"""Requirements"""

import random
import pygame as py

# Window
w, h = 800, 608


class Racket:
    """Racket class."""

    def __init__(self, parent_window, x, y, width, height, ball):
        self.parent_window = parent_window
        self.x = x
        self.y = y
        self.y_speed = 0.7
        self.width = width
        self.height = height
        self.color = (255, 255, 255)
        self.ball = ball

    def draw(self):
        """Draws a racket."""
        py.draw.rect(
            self.parent_window, self.color, (self.x, self.y, self.width, self.height)
        )

    def move_up(self, y_speed):
        """Moves the racket up."""
        if self.y >= 0:
            self.y -= y_speed

    def move_down(self, y_speed):
        """Moves the racket down."""
        if self.y <= h - self.height:
            self.y += y_speed

    def computer_movement(self):
        """Moves the computer racket."""
        computer_y_speed = 0.7
        if self.ball.x < w // 2:
            if self.y < self.ball.y:
                self.move_down(computer_y_speed)
            elif self.y > self.ball.y:
                self.move_up(computer_y_speed)


class Ball:
    """Ball class."""

    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.x = random.randint(w // 2 - 32, w // 2 + 32)
        self.y = random.randint(h // 2 - 32, h // 2 + 32)
        self.color = (255, 255, 255)
        self.x_speed = 0.5
        self.y_speed = 0.5
        print(self.x, self.y)

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
        self.score_r1 = 0
        self.score_r2 = 0

    # Collisions
    def border_collision(self):
        """Checks for border collision."""
        if self.ball.y < 0 or self.ball.y > h:
            self.ball.y_speed *= -1
            self.ball.x_speed += self.ball.x_speed / 4
            return False
        if self.ball.x < 0:
            self.restart()
            return True
        if self.ball.x > w:
            self.restart()
            return True
        return False

    def racket_collision(self):
        """Checks for racket collision."""
        if (
            self.ball.x < self.racket1.x + self.racket1.width
            and self.ball.y > self.racket1.y
            and self.ball.y < self.racket1.y + self.racket1.height
        ):
            self.ball.x_speed *= -1
        if (
            self.ball.x > self.racket2.x
            and self.ball.y > self.racket2.y
            and self.ball.y < self.racket2.y + self.racket2.height
        ):
            self.ball.x_speed *= -1

    def show_score(self):
        """Shows the score."""
        score_font = py.font.Font("freesansbold.ttf", 32)
        score_r1_text = score_font.render(f"{self.score_r1}", True, (255, 255, 255))
        score_r2_text = score_font.render(f"{self.score_r2}", True, (255, 255, 255))
        self.window.blit(score_r1_text, (32, 32))
        self.window.blit(score_r2_text, (w - 48, 32))

    def update_score(self):
        """Updates the score."""
        is_border_collision = self.border_collision()
        if self.ball.x > w // 2 and is_border_collision:
            self.score_r1 += 1
        if self.ball.x < w // 2 and is_border_collision:
            self.score_r2 += 1

    def restart(self):
        """Restarts the game."""
        print("foo")
        self.ball.x, self.ball.y = w // 2, h // 2
        self.ball.x_speed, self.ball.y_speed = 0.5, 0.5
        self.racket1.x, self.racket1.y = 5, 288
        self.racket1.width, self.racket1.height = 10, 75
        self.racket2.x, self.racket2.y = 785, 288
        self.racket2.width, self.racket2.height = 10, 75
        self.update_score()

    def game_over(self):
        """Displays \"GAME OVER\"."""
        self.ball.x = 1000
        self.ball.x_speed, self.ball.y_speed = 0, 0
        self.racket1.x, self.racket2.x = -500, -500
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

            # Color
            self.window.fill((0, 0, 0))

            # Racket Control
            if py.key.get_pressed()[py.K_UP]:
                self.racket2.move_up(self.racket2.y_speed)
            if py.key.get_pressed()[py.K_DOWN]:
                self.racket2.move_down(self.racket2.y_speed)

            # Drawing & Movement
            self.ball.draw()
            self.ball.move()
            self.racket1.draw()
            self.racket2.draw()
            self.racket1.computer_movement()

            # Score
            self.show_score()
            self.update_score()

            # Check Collision & Boundary
            self.border_collision()
            self.racket_collision()
            py.display.update()


# Running the game
if __name__ == "__main__":
    game = Game()
    game.run()
