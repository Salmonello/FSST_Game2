import pygame
from load_image import *
from entities import *
from camera import *

ACC = 0.5
GROUND_HEIGHT = HEIGHT - 100


def player_movement(keys_pressed):
    if keys_pressed[pygame.K_a]: # LEFT
        player.X -= player.X_VEL
        player.is_RUN_LEFT = True
    else:
        player.is_RUN_LEFT = False

    if keys_pressed[pygame.K_d]: # RIGHT
        player.X += player.X_VEL
        player.is_RUN_RIGHT = True
    else:
        player.is_RUN_RIGHT = False

def jumping_gravity(keys_pressed):
    if player.Y + player.HEIGHT + player.Y_VEL < GROUND_HEIGHT: # FALLING 
        player.Y_VEL += ACC
        player.Y += player.Y_VEL
        player.is_FALL = True
        player.is_RUN_RIGHT = False
        player.is_RUN_LEFT = False
    else:
        player.Y = GROUND_HEIGHT - player.HEIGHT
        player.Y_VEL = 0
        player.is_FALL = False
    
        if keys_pressed[pygame.K_w]:
            player.Y_VEL = 0
            player.Y_VEL -= player.JUMP_POW