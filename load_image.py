import pygame
import os
from entities import *

WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])


class Entity_image:
    def __init__(self, STANDING, RUNNING_LEFT, RUNNING_RIGHT, FALLING):
        self.STANDING = STANDING
        self.RUNNING_LEFT = RUNNING_LEFT
        self.RUNNING_RIGHT = RUNNING_RIGHT
        self.FALLING = FALLING



PLAYER_STANDING = [pygame.image.load(os.path.join('Player_IMG', 'standing_1.png')), 
                    pygame.image.load(os.path.join('Player_IMG', 'standing_2.png')), 
                    pygame.image.load(os.path.join('Player_IMG', 'standing_3.png')), 
                    pygame.image.load(os.path.join('Player_IMG', 'standing_4.png')),
                    pygame.image.load(os.path.join('Player_IMG', 'standing_4.png')), 
                    pygame.image.load(os.path.join('Player_IMG', 'standing_3.png')), 
                    pygame.image.load(os.path.join('Player_IMG', 'standing_2.png')), 
                    pygame.image.load(os.path.join('Player_IMG', 'standing_1.png'))]

PLAYER_STANDING = [pygame.transform.scale(
    PLAYER_STANDING[0], (player.WIDTH, player.HEIGHT)), 
                    pygame.transform.scale(
    PLAYER_STANDING[1], (player.WIDTH, player.HEIGHT)), 
                    pygame.transform.scale(
    PLAYER_STANDING[2], (player.WIDTH, player.HEIGHT)), 
                    pygame.transform.scale(
    PLAYER_STANDING[3], (player.WIDTH, player.HEIGHT)),
                    pygame.transform.scale(
    PLAYER_STANDING[4], (player.WIDTH, player.HEIGHT)), 
                    pygame.transform.scale(
    PLAYER_STANDING[5], (player.WIDTH, player.HEIGHT)), 
                    pygame.transform.scale(
    PLAYER_STANDING[6], (player.WIDTH, player.HEIGHT)), 
                    pygame.transform.scale(
    PLAYER_STANDING[7], (player.WIDTH, player.HEIGHT))]




PLAYER_RUNNING_LEFT = [pygame.image.load(os.path.join('Player_IMG', 'run_left_1.png')), 
                        pygame.image.load(os.path.join('Player_IMG', 'run_left_2.png')), 
                        pygame.image.load(os.path.join('Player_IMG', 'run_left_3.png')), 
                        pygame.image.load(os.path.join('Player_IMG', 'run_left_4.png'))]

PLAYER_RUNNING_LEFT = [pygame.transform.scale(
    PLAYER_RUNNING_LEFT[0], (player.WIDTH, player.HEIGHT)), 
                    pygame.transform.scale(
    PLAYER_RUNNING_LEFT[1], (player.WIDTH, player.HEIGHT)), 
                    pygame.transform.scale(
    PLAYER_RUNNING_LEFT[2], (player.WIDTH, player.HEIGHT)), 
                    pygame.transform.scale(
    PLAYER_RUNNING_LEFT[3], (player.WIDTH, player.HEIGHT))]




PLAYER_RUNNING_RIGHT = [pygame.image.load(os.path.join('Player_IMG', 'run_right_1.png')), 
                        pygame.image.load(os.path.join('Player_IMG', 'run_right_2.png')), 
                        pygame.image.load(os.path.join('Player_IMG', 'run_right_3.png')), 
                        pygame.image.load(os.path.join('Player_IMG', 'run_right_4.png'))]

PLAYER_RUNNING_RIGHT = [pygame.transform.scale(
    PLAYER_RUNNING_RIGHT[0], (player.WIDTH, player.HEIGHT)), 
                    pygame.transform.scale(
    PLAYER_RUNNING_RIGHT[1], (player.WIDTH, player.HEIGHT)), 
                    pygame.transform.scale(
    PLAYER_RUNNING_RIGHT[2], (player.WIDTH, player.HEIGHT)), 
                    pygame.transform.scale(
    PLAYER_RUNNING_RIGHT[3], (player.WIDTH, player.HEIGHT))]

PLAYER_FALLING = pygame.image.load(
    os.path.join('Player_IMG', 'falling.png'))
PLAYER_FALLING = pygame.transform.scale(
    PLAYER_FALLING, (player.WIDTH, player.HEIGHT))


PLAYER_IMG = Entity_image(PLAYER_STANDING, PLAYER_RUNNING_LEFT, PLAYER_RUNNING_RIGHT, PLAYER_FALLING)