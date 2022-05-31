""" All shared variables"""
from pygame import Vector2

SCREEN_SIZE = 900, 900

EMPTY = 0
BLOCK = 1
H_BLOCK = 2

IMG_SIZE = 150

X_VEC = Vector2(1, 0.5) * 0.5
Z_VEC = Vector2(-1, 0.5) * 0.5
Y_VEC = Vector2(0, 1) * 0.5

Y_PLAYER_VEC = Vector2(0, 0.125)

MAX_FPS = 100


OFFSET = SCREEN_SIZE[0] / 2 - IMG_SIZE / 2, 0
