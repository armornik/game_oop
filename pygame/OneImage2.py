# Import packages
import pygame
# from pygame.locals import *
import sys
from pathlib import Path

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# Путь к папке где находится файл
BASE_PATH = Path(__file__).resolve().parent
print(BASE_PATH)

# Build a path to the file in the images folder
path_to_ball = f'{BASE_PATH}/images/ball.png'
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

# 5 - Initialize variables

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

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    # draw ball at position 100 across (x) and 200 down (y)
    window.blit(ballImage, (100, 200))

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
