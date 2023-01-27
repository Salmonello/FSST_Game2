import pygame
from camera import *
from load_image import *
from events import *

def draw_win():
    WINDOW.fill([60,60,60])
    pygame.draw.rect(WINDOW, [0,0,50], [0 - camera.POS_X, GROUND_HEIGHT - camera.POS_Y, WIDTH, HEIGHT - GROUND_HEIGHT])
    

    if player.is_RUN_LEFT:
        player.ANIM_COUNT += 0.2
        if player.ANIM_COUNT + 0.2 > 4:
            player.ANIM_COUNT = 0
        WINDOW.blit(PLAYER_IMG.RUNNING_LEFT[int(player.ANIM_COUNT)], [player.X - camera.POS_X, player.Y - camera.POS_Y])

    elif player.is_RUN_RIGHT:
        player.ANIM_COUNT += 0.2
        if player.ANIM_COUNT + 0.2 > 4:
            player.ANIM_COUNT = 0
        WINDOW.blit(PLAYER_IMG.RUNNING_RIGHT[int(player.ANIM_COUNT)], [player.X - camera.POS_X, player.Y - camera.POS_Y])

    elif player.is_FALL:
        WINDOW.blit(PLAYER_IMG.FALLING, [player.X - camera.POS_X, player.Y - camera.POS_Y])

    else:
        player.ANIM_COUNT += 0.2
        if player.ANIM_COUNT + 0.2 > 8:
            player.ANIM_COUNT = 0
        WINDOW.blit(PLAYER_IMG.STANDING[int(player.ANIM_COUNT)], [player.X - camera.POS_X, player.Y - camera.POS_Y])

    pygame.display.update()