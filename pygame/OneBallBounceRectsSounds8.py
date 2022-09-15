# Import packages
import pygame
# from pygame.locals import *
import sys
from pathlib import Path
import random

# 2 - Define constants
GRAY = (230, 230, 230)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
TEAL = (0, 255, 255)
PURPLE = (255, 0, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

# Путь к папке где находится файл
BASE_PATH = Path(__file__).resolve().parent
print(BASE_PATH)

# Build a path to the file in the images folder
path_to_ball = f'{BASE_PATH}/Images/ball.png'
print(path_to_ball)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# create a clock object, which will be used at the bottom
# создания объект часов, который будет использоваться в конце нашего основного цикла для поддержания
# нашей максимальной частоты кадров
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load(path_to_ball)
bounceSound = pygame.mixer.Sound(f'{BASE_PATH}/Sounds/boing.wav')
pygame.mixer.music.load(f'{BASE_PATH}/Sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0)

# 5 - Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    #  get a list of the events that happened
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed  # reverse X direction
        bounceSound.play()

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction
        bounceSound.play()

    # Update the ball's location, using the speed in two directions
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    window.blit(ballImage, ballRect)
    # Draw a box
    pygame.draw.line(window, BLUE, (20, 20), (60, 20), 4)  # top
    pygame.draw.line(window, BLUE, (20, 20), (20, 60), 4)  # left
    pygame.draw.line(window, BLUE, (20, 60), (60, 60), 4)  # right
    pygame.draw.line(window, BLUE, (60, 20), (60, 60), 4)  # bottom
    # Draw an X in the box
    pygame.draw.line(window, BLUE, (20, 20), (60, 60), 1)
    pygame.draw.line(window, BLUE, (20, 60), (60, 20), 1)

    # Draw a filled circle and an empty circle
    pygame.draw.circle(window, GREEN, (250, 50), 30, 0)  # filled
    pygame.draw.circle(window, GREEN, (400, 50), 30, 2)  # 2 pixel edge
    # Draw a filled rectangle and an empty rectangle
    pygame.draw.rect(window, RED, (250, 150, 100, 50), 0)  # filled
    pygame.draw.rect(window, RED, (400, 150, 100, 50), 1)  # 1 pixel edge

    # Draw a filled ellipse and an empty ellipse
    pygame.draw.ellipse(window, YELLOW, (250, 250, 80, 40), 0)  # filled
    pygame.draw.ellipse(window, YELLOW, (400, 250, 80, 40), 2)  # 2 pixel edge
    # Draw a six-sided polygon
    pygame.draw.polygon(window, TEAL, ((240, 350), (350, 350), (410, 410), (350, 470), (240, 470), (170, 410)))
    # Draw an arc
    pygame.draw.arc(window, BLUE, (20, 400, 100, 100), 0, 2, 5)

    # Draw anti-aliased lines: a single line, then a list of points
    pygame.draw.aaline(window, RED, (500, 400), (540, 470), 1)
    pygame.draw.aalines(window, BLUE, True, ((580, 400), (587, 450), (595, 460), (600, 444)), 1)

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
