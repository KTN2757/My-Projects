import random
import math
import time
import pygame


# Initializing
pygame.init()

# Window
w, h = 800, 600
window = pygame.display.set_mode((w, h))
logo = pygame.image.load("snake.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Snake Game by KTN.")


# Snake
class Snake:
    color = (0, 255, 0)
    xChange = 32
    yChange = 0
    w = 32
    h = 32
    x = (400 // w) * w
    y = (300 // h) * h


def snake(x, y, color):
    pygame.draw.rect(window, color, (x, y, Snake.w, Snake.h))


# Food
foodImg = pygame.image.load("apple.png")


class Food:
    x = ((random.randint(32, w - 32)) // 32) * 32
    y = ((random.randint(32, h - 32)) // 32) * 32


def food(x, y):
    window.blit(foodImg, (x, y))


# Collision
def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))
    if distance < 31:
        return True
    else:
        return False


# Score
score = 0
scoreFont = pygame.font.Font("freesansbold.ttf", 32)
scoreText = scoreFont.render(f"Score: {score}", True, (255, 255, 255))

# Game Over
gameOverFont = pygame.font.Font("freesansbold.ttf", 64)


def gameOver():
    gameOverText = gameOverFont.render("GAME OVER", True, (255, 255, 255))
    window.blit(gameOverText, (200, 250))
    Snake.x, Snake.y = 1000, 1000


# Restart The Game
restartFont = pygame.font.Font("freesansbold.ttf", 16)


def restart():
    restartText = restartFont.render(
        "Press 'r' to restart the game or 'q' to quit the game.", True, (255, 255, 255)
    )
    window.blit(restartText, (200, 350))


# a = 3
dumbScoreList = []
smartScoreList = []

running = True
# Game Loop
while running:
    time.sleep(0.2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Snake.yChange = 0
                Snake.xChange = 32
            if event.key == pygame.K_LEFT:
                Snake.yChange = 0
                Snake.xChange = -32
            if event.key == pygame.K_UP:
                Snake.xChange = 0
                Snake.yChange = -32
            if event.key == pygame.K_DOWN:
                Snake.xChange = 0
                Snake.yChange = 32
            if event.key == pygame.K_r:
                score = 0
                scoreText = scoreFont.render(f"Score: {score}", True, (255, 255, 255))
                Snake.x = ((400) // 32) * 32
                Snake.y = ((300) // 32) * 32
                snake(Snake.x, Snake.y, Snake.color)
            if event.key == pygame.K_q:
                running = False

    # Intial Movement
    Snake.x += Snake.xChange
    Snake.y += Snake.yChange

    # Color
    window.fill((0, 0, 0))

    # Calling Snake and Food
    food(Food.x, Food.y)
    snake(Snake.x, Snake.y, (255, 0, 0))

    # Calling Collision and Growing Snake

    foodCollision = isCollision(Snake.x, Snake.y, Food.x, Food.y)
    if foodCollision:
        score += 1
        scoreText = scoreFont.render(f"Score: {score}", True, (255, 255, 255))
        Food.x = ((random.randint(32, w - 32)) // 32) * 32
        Food.y = ((random.randint(32, h - 32)) // 32) * 32

    if score >= 1:
        dumbScoreList.append(score)
        for i in dumbScoreList:
            if i not in smartScoreList:
                smartScoreList.append(i)
        print(smartScoreList)
        newSnakeY = Snake.y
        for i in range(1, score + 1):
            newSnakeX = ((Snake.x - Snake.w * i) // 32) * 32
            if Snake.yChange == 0 and Snake.xChange == 32:
                # Right
                pass
            if Snake.yChange == 0 and Snake.xChange == -32:
                # Left
                newSnakeX += 64 * i
            if Snake.xChange == 0 and Snake.yChange == -32:
                # Up
                newSnakeX += 32 * i
                newSnakeY += 32
            if Snake.xChange == 0 and Snake.yChange == 32:
                # Down
                newSnakeX += 32 * i
                newSnakeY -= 32
            snake(newSnakeX, newSnakeY, Snake.color)
        print(newSnakeX, newSnakeY)
    window.blit(scoreText, (0, 0))

    # Border
    if Snake.x <= 0:
        gameOver()
    elif Snake.x >= (w - Snake.w):
        gameOver()
    if Snake.y <= 0:
        gameOver()
    elif Snake.y >= (h - Snake.h):
        gameOver()

    # Restart The Game
    if Snake.x == 1000:
        restart()
    pygame.display.update()
pygame.quit()
