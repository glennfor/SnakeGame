############################
###      Game    ###########
###########################

#[game]
import pygame
import pygame.locals

pygame.init()
pygame.mixer.init()
pygame.font.init()

#[utils]
import os
import time
import random

############################
#####   REOUSRCES    #######
############################

#using dimmer shades
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 255, 0)

YELLOW = (255, 255, 0)

BORDER_COLOR = BLUE
BACKGROUND_COLOR = BLACK
SNAKE_COLOR = GREEN
FOOD_COLOR = RED

LINE_COLOR = WHITE

SNAKE_SPEED = 100 /1000

#[GAME]
FPS = 30

IMPRESSION_TIME = 1000 / 1000

GRID_WIDTH = 40
GRID_HEIGHT = 25


START = (GRID_WIDTH//2, GRID_HEIGHT//2)

#directions
#due to pygames coorinate system y increases downward and reduces upward
DIRECTIONS = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT':(1, 0),
}

#[WINDOW]
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
MIN_MARGIN = 50

BOX_SIZE = min((WINDOW_WIDTH - MIN_MARGIN)//GRID_WIDTH , (WINDOW_HEIGHT - MIN_MARGIN)//GRID_HEIGHT)
WINDOW_MARGIN_X = (WINDOW_WIDTH - GRID_WIDTH*BOX_SIZE) // 2
WINDOW_MARGIN_Y = (WINDOW_HEIGHT - GRID_HEIGHT*BOX_SIZE) // 2 

GRID_BORDER = 8

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.DOUBLEBUF, 32)
pygame.display.set_caption("Snake Game")

#main font

font = pygame.font.SysFont('Deja Vu Sans', 50, True)

#[SOUNDS]
MUNCH = pygame.mixer.Sound('./assets/munch.wav')

pygame.mixer.music.load('./assets/gamemusic.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)

print("✔🕙 All resources loaded...")
