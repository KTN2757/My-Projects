"""Requirements."""

import math
import random
import time
import pygame

# Window size constants
w, h = 800, 600


# Snake
class Snake:
    """Snake class."""

    def __init__(self, parent_window, length):
        self.parent_window = parent_window
        self.color = (0, 255, 0)
        self.x_change = 32
        self.y_change = 0
        self.w = 32
        self.h = 32
        self.length = length
        self.x = [(400 // self.w) * self.w] * self.length
        self.y = [(300 // self.h) * self.h] * self.length
        self.direction = "right"

    def increase_length(self):
        """Increases the length of the snake."""
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        """Draws a snake."""
        for i in range(self.length):
            pygame.draw.rect(
                self.parent_window, self.color, (self.x[i], self.y[i], self.w, self.h)
            )

    def move_left(self):
        """Moves the snake left"""
        if self.direction != "right":
            self.direction = "left"

    def move_right(self):
        """Moves the snake right"""
        if self.direction != "left":
            self.direction = "right"

    def move_up(self):
        """Moves the snake up"""
        if self.direction != "down":
            self.direction = "up"

    def move_down(self):
        """Moves the snake down"""
        if self.direction != "up":
            self.direction = "down"

    def move(self):
        """Moves the snake"""
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        self.x[0] += self.x_change
        self.y[0] += self.y_change
        if self.direction == "up":
            self.x_change = 0
            self.y_change = -32
        if self.direction == "down":
            self.x_change = 0
            self.y_change = 32
        if self.direction == "left":
            self.x_change = -32
            self.y_change = 0
        if self.direction == "right":
            self.x_change = 32
            self.y_change = 0


# Food
class Food:
    """Food class."""

    def __init__(self, parent_window):
        self.parent_window = parent_window
        self.x = ((random.randint(32, w - 32)) // 32) * 32
        self.y = ((random.randint(32, h - 32)) // 32) * 32
        self.food_img = pygame.image.load("apple.png")

    def spawn(self):
        """Spawn food."""
        self.parent_window.blit(self.food_img, (self.x, self.y))


# Main Game
class Game:
    """Main game."""

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((w, h))
        logo = pygame.image.load("snake.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Snake Game by KTN.")
        self.default_snake_length = 2
        self.snake = Snake(self.window, self.default_snake_length)
        self.snake.draw()
        self.food = Food(self.window)
        self.is_game_over = False
        self.score = 0

    def display_score(self):
        """Displays the score"""
        score_font = pygame.font.Font("freesansbold.ttf", 32)
        score_text = score_font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(score_text, (32, 32))

    def update_score(self, score):
        """Updates the score"""
        self.score += score
        self.display_score()

    def reset_score(self):
        """Resets the score"""
        self.score = 0
        self.display_score()

    def is_collision(self, x1, y1, x2, y2):
        """Checks collision."""
        distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))
        return distance < 31

    def food_collision(self):
        """Calling collision and growing snake"""
        food_collision = self.is_collision(
            self.snake.x[0], self.snake.y[0], self.food.x, self.food.y
        )
        if food_collision:
            self.update_score(1)
            self.food.x = ((random.randint(32, w - 32)) // 32) * 32
            self.food.y = ((random.randint(32, h - 32)) // 32) * 32
            self.snake.increase_length()

    def border_collision(self):
        """Checks border collision."""
        if self.snake.x[0] <= 0:
            self.is_game_over = self.game_over()
        elif self.snake.x[0] >= (w - self.snake.w):
            self.is_game_over = self.game_over()
        if self.snake.y[0] <= 0:
            self.is_game_over = self.game_over()
        elif self.snake.y[0] >= (h - self.snake.h):
            self.is_game_over = self.game_over()

    def restart(self):
        """Restarts the game."""
        self.is_game_over = False
        self.reset_score()
        self.snake.length = self.default_snake_length
        self.snake.direction = "right"
        self.snake.x = [(400 // self.snake.w) * self.snake.w] * self.snake.length
        self.snake.y = [(300 // self.snake.h) * self.snake.h] * self.snake.length
        self.food.x = ((random.randint(32, w - 32)) // 32) * 32
        self.food.y = ((random.randint(32, h - 32)) // 32) * 32
        self.snake.draw()

    def game_over(self):
        """Displays \"GAME OVER\"."""
        for i in range(self.snake.length):
            self.snake.x[i], self.snake.y[i] = 1000, 1000
        game_over_font = pygame.font.Font("freesansbold.ttf", 64)
        restart_font = pygame.font.Font("freesansbold.ttf", 16)
        game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
        restart_text = restart_font.render(
            "Press 'r' to restart the game or 'q' to quit the game.",
            True,
            (255, 255, 255),
        )
        self.window.blit(game_over_text, (200, 250))
        self.window.blit(restart_text, (200, 350))
        return True

    def run(self):
        """Runs the game."""
        running = True
        # Game Loop
        while running:
            time.sleep(0.2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.snake.move_right()
                    if event.key == pygame.K_LEFT:
                        self.snake.move_left()
                    if event.key == pygame.K_UP:
                        self.snake.move_up()
                    if event.key == pygame.K_DOWN:
                        self.snake.move_down()
                    if self.is_game_over:
                        if event.key == pygame.K_r:
                            self.restart()
                        if event.key == pygame.K_q:
                            running = False

            # Initial Movement
            self.snake.move()

            # Color
            self.window.fill((0, 0, 0))

            # Score
            self.display_score()

            # Calling Snake and Food
            self.food.spawn()
            self.snake.draw()

            # Check collisions
            self.food_collision()
            self.border_collision()

            pygame.display.update()
        pygame.quit()


# Initializing
if __name__ == "__main__":
    game = Game()
    game.run()
