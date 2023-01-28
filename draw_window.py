import pygame
from load_image import *
import events
import random
import entities

kaktusx=[random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716),random.randint(640, 716)]
kaktusy=[random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610),random.randint(475, 610)]

cloudsx= [random.randint(100, 500),random.randint(200, 900),random.randint(100, 900),random.randint(200, 900)]
cloudsy= [random.randint(50, 100),random.randint(100, 200),random.randint(50, 100),random.randint(100, 200)]

other_player = entities.Entity(20, 20, 100, 200, 8, 0, 14)
other_bullets = Projectile(-10, -10, 8, 8, 20)

def set_other_player(player):
    global other_player
    other_player = player

def set_other_bullets(bullet):
    global other_bullets
    other_bullets = bullet

def draw_win():
    global other_player

    WINDOW.fill([120,150,255])

    #drawing sun
    pygame.draw.rect(WINDOW,[255,255,0],[500, 180, 50, 50])

    # drawing cactus
    cactus_RECT = pygame.Rect(640, 475, 80, 160)
    pygame.draw.rect(WINDOW, [0,100,0], cactus_RECT)

    #cactus dots
    pygame.draw.rect(WINDOW, [0, 0, 0], [636, 480, 4, 4])
    pygame.draw.rect(WINDOW, [0, 0, 0], [638, 580, 4, 4])
    pygame.draw.rect(WINDOW, [0, 0, 0], [640, 520, 4, 4])
    pygame.draw.rect(WINDOW, [0, 0, 0], [638, 530, 4, 4])
    pygame.draw.rect(WINDOW, [0, 0, 0], [636, 500, 4, 4])
    pygame.draw.rect(WINDOW, [0, 0, 0], [720, 480, 4, 4])
    pygame.draw.rect(WINDOW, [0, 0, 0], [718, 520, 4, 4])
    pygame.draw.rect(WINDOW, [0, 0, 0], [720, 570, 4, 4])
    pygame.draw.rect(WINDOW, [0, 0, 0], [718, 510, 4, 4])
    pygame.draw.rect(WINDOW, [0, 0, 0], [719, 545, 4, 4])

    pygame.draw.rect(WINDOW, [0, 0, 0], [670, 471, 4, 4])
    pygame.draw.rect(WINDOW, [0, 0, 0], [700, 473, 4, 4])

    for i in range(1, 18):
        pygame.draw.rect(WINDOW, [0, 0, 0], [kaktusx[i], kaktusy[i], 4, 4])

    #drawing clouds
    pygame.draw.rect(WINDOW,[240,240,240],[cloudsx[0], cloudsy[0], 300, 80])
    pygame.draw.rect(WINDOW,[240,240,240],[cloudsx[1], cloudsy[1], 140, 40])
    pygame.draw.rect(WINDOW,[240,240,240],[cloudsx[2], cloudsy[2], 100, 40])
    pygame.draw.rect(WINDOW,[240,240,240],[cloudsx[3], cloudsy[3], 200, 80])

    #Ground
    ground_RECT = pygame.Rect(0, events.GROUND_HEIGHT, WIDTH, HEIGHT - events.GROUND_HEIGHT)
    pygame.draw.rect(WINDOW,[255,255,80],ground_RECT)

    #drawing bullet
    pygame.draw.rect(WINDOW,(0,0,0),[bullet.x, bullet.y, bullet.width, bullet.height])

    #drawing bullet
    pygame.draw.rect(WINDOW,(0,0,0),[other_bullets.x, other_bullets.y, other_bullets.width, other_bullets.height])
    
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