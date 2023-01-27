import pygame
from load_image import *
from events import *
import random
import entities

kaktusx=[random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716)]
kaktusy=[random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610)]

other_player = entities.Entity(20, 20, 100, 200, 8, 0, 14)
other_bullets = Projectile(-10, -10, 8, 8, 20)

def set_other_player(player):
    global other_player
    other_player = player

def draw_win():
    WINDOW.fill([60,60,60])
    pygame.draw.rect(WINDOW, [0,0,50], [0 - camera.POS_X, GROUND_HEIGHT - camera.POS_Y, WIDTH, HEIGHT - GROUND_HEIGHT])

    #drawing sun
    pygame.draw.rect(WINDOW,[255,255,0],[500, 180, 50, 50])

    # drawing cactus
    cactus_RECT = pygame.Rect(640, 475, 80, 160)
    pygame.draw.rect(WINDOW, [0,100,0], cactus_RECT)

    #cactus dots
    for i in range(1, 18):
        pygame.draw.rect(WINDOW, [0, 0, 0], [kaktusx[i], kaktusy[i], 4, 4])

    #drawing clouds
    pygame.draw.rect(WINDOW,[240,240,240],[200, 70, 140, 40])
    pygame.draw.rect(WINDOW,[240,240,240],[900, 180, 300, 80])

    ground_RECT = pygame.Rect(0, GROUND_HEIGHT, WIDTH, HEIGHT - GROUND_HEIGHT)
    pygame.draw.rect(WINDOW,[255,255,80],ground_RECT)

    #drawing bullet
    pygame.draw.rect(WINDOW,"black",[bullet.x, bullet.y, bullet.width, bullet.height])

    #draw other bullet
    pygame.draw.rect(WINDOW,"black",[other_bullets.x, other_bullets.y, other_bullets.width, other_bullets.height])
    

    #draw other player
    if other_player.is_RUN_LEFT and not other_player.is_RUN_RIGHT:
        other_player.ANIM_COUNT += 0.2
        if other_player.ANIM_COUNT + 0.2 > 4:
            other_player.ANIM_COUNT = 0
        WINDOW.blit(PLAYER_IMG.RUNNING_LEFT[int(other_player.ANIM_COUNT)], [other_player.X, other_player.Y])

    elif other_player.is_RUN_RIGHT and not other_player.is_RUN_LEFT:
        other_player.ANIM_COUNT += 0.2
        if other_player.ANIM_COUNT + 0.2 > 4:
            other_player.ANIM_COUNT = 0
        WINDOW.blit(PLAYER_IMG.RUNNING_RIGHT[int(other_player.ANIM_COUNT)], [other_player.X, other_player.Y])

    elif other_player.is_FALL:
        WINDOW.blit(PLAYER_IMG.FALLING, [other_player.X, other_player.Y])

    else:
        other_player.ANIM_COUNT += 0.2
        if other_player.ANIM_COUNT + 0.2 > 8:
            other_player.ANIM_COUNT = 0
        WINDOW.blit(PLAYER_IMG.STANDING[int(other_player.ANIM_COUNT)], [other_player.X, other_player.Y])


    #draw real player
    if player.is_RUN_LEFT and not player.is_RUN_RIGHT:
        player.ANIM_COUNT += 0.2
        if player.ANIM_COUNT + 0.2 > 4:
            player.ANIM_COUNT = 0
        WINDOW.blit(PLAYER_IMG.RUNNING_LEFT[int(player.ANIM_COUNT)], [player.X, player.Y])

    elif player.is_RUN_RIGHT and not player.is_RUN_LEFT:
        player.ANIM_COUNT += 0.2
        if player.ANIM_COUNT + 0.2 > 4:
            player.ANIM_COUNT = 0
        WINDOW.blit(PLAYER_IMG.RUNNING_RIGHT[int(player.ANIM_COUNT)], [player.X, player.Y])

    elif player.is_FALL:
        WINDOW.blit(PLAYER_IMG.FALLING, [player.X, player.Y])

    else:
        player.ANIM_COUNT += 0.2
        if player.ANIM_COUNT + 0.2 > 8:
            player.ANIM_COUNT = 0
        WINDOW.blit(PLAYER_IMG.STANDING[int(player.ANIM_COUNT)], [player.X, player.Y])

    pygame.display.update()