import pygame
from load_image import *
from entities import *
from pygame import mixer
from draw_window import *
pygame.mixer.init()


ACC = 0.5
GROUND_HEIGHT = HEIGHT - 100
cactus_RECT = pygame.Rect(640, 475, 80, 160)
ground_RECT = pygame.Rect(0, GROUND_HEIGHT, WIDTH, HEIGHT - GROUND_HEIGHT)
#shot_sound.set_volume(0.05)
hitmarker_sound = mixer.music.load('Audio/hitmarker.mp3')

#step_sound= mixer.Sound('Audio/steps.mp3')
#step_sound.play(-1)
entry= pygame.mixer.Sound("Audio/entry.mp3")
entry.set_volume(0.07)
entry.play()

mixer.music.load('Audio/backgroundmusic.mp3')
mixer.music.set_volume(0.015)
mixer.music.play(-1)
"""
mixer.music.load('Audio/steps.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)
"""
shot= pygame.mixer.Sound("Audio/shot.mp3")
shot.set_volume(0.025)
hitmarker= pygame.mixer.Sound("Audio/hitmarker.mp3")
hitmarker.set_volume(0.025)

def player_movement(keys_pressed):
    player_RECT = pygame.Rect(player.X, player.Y, player.WIDTH, player.HEIGHT)
    if keys_pressed[pygame.K_a] and not ((player_RECT.midleft < cactus_RECT.midright and player_RECT.midright >= cactus_RECT.midleft) and player_RECT.centery >= cactus_RECT.centery-100): # LEFT
        player.X -= player.X_VEL
        player.is_RUN_LEFT = True

    else:
        player.is_RUN_LEFT = False

    if keys_pressed[pygame.K_d] and not ((player_RECT.midright > cactus_RECT.midleft and player_RECT.midleft <= cactus_RECT.midright) and player_RECT.centery >= cactus_RECT.centery-100):
        player.X += player.X_VEL
        player.is_RUN_RIGHT = True

    else:
        player.is_RUN_RIGHT = False



def jumping_gravity(keys_pressed):
    if player.is_FALL: # FALLING 
        player.Y_VEL += ACC
        player.Y += player.Y_VEL
        player.is_RUN_RIGHT = False
        player.is_RUN_LEFT = False
    else:
        player.Y = GROUND_HEIGHT - player.HEIGHT
        player.Y_VEL = 0
    
        if keys_pressed[pygame.K_w]:
            player.Y -= 1
            player.Y_VEL -= player.JUMP_POW

def collision_detection():
    player_RECT = pygame.Rect(player.X, player.Y, player.WIDTH, player.HEIGHT)

    if player_RECT.bottom >= ground_RECT.top:
        player.is_FALL = False
    else:
        player.is_FALL = True

def shoot_right(keys_pressed):
    if keys_pressed[pygame.K_RIGHT] and not bullet.is_shoot_R and not bullet.is_shoot_L:
        bullet.is_shoot_R = True
        bullet.x = player.X + player.WIDTH / 2 +30
        bullet.y = player.Y + player.HEIGHT / 2 -10
        shot.play()
    if bullet.is_shoot_R:
        bullet.x += bullet.vel
        if (bullet.x >= 650 and bullet.y>=475) and not bullet.x >= 700 and bullet.y>=475:
            bullet.is_shoot_R = False
            hitmarker.play()

        if bullet.x > WIDTH:
            bullet.is_shoot_R = False


def shoot_left(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and not bullet.is_shoot_R and not bullet.is_shoot_L:
        bullet.is_shoot_L = True
        bullet.x = player.X + player.WIDTH / 2 -30
        bullet.y = player.Y + player.HEIGHT / 2 -10
        shot.play()
    if bullet.is_shoot_L:
        bullet.x -= bullet.vel
        if (bullet.x <= 700 and bullet.y>=475) and not bullet.x <= 620 and bullet.y>=475:
            bullet.is_shoot_L = False
            hitmarker.play()

        if bullet.x < -10:
            bullet.is_shoot_L = False

def checkbullet_hit(other_player, bullet):
    global score_eigen
    if other_player.RECT == bullet.x and other_player.RECT == bullet.y:
        score_eigen+=1

def checkbullet_gothit(player, other_bullets):
    global score_gegner
    if player.RECT == other_bullets.x and player.RECT == other_bullets.y:
        score_gegner+=1