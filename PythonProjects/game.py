import pygame
import random
import math


WIDTH, HEIGHT = 900,600
PLAYER_WIDTH, PLAYER_HEIGHT = 10, 40
MAX_VEL = 5


pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wells")
entities = []


class Entity:

    x, y = 0, 0
    on_screen = True
    rect = pygame.Rect(x,y,x,y)
    color = "green"

    def __init__(e;f, x=random.random()*WIDTH, y=random.random()*HEIGHT, WIDTH=PLAYER_WIDTH, height=PLAYER_HEIGHT):
    