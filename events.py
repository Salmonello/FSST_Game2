import pygame
from load_image import *
from entities import *
from pygame import mixer
from draw_window import *
pygame.mixer.init()



ACC = 0.5
GROUND_HEIGHT = HEIGHT - 100                        #Ground höhe festlegen
cactus_RECT = pygame.Rect(640, 475, 80, 160)                   #kactus und dazu gehöriges Rectangle erstellen
ground_RECT = pygame.Rect(0, GROUND_HEIGHT, WIDTH, HEIGHT - GROUND_HEIGHT)          #ground Rectangle erstellen

entry= pygame.mixer.Sound("Audio/entry.mp3")                #sound zum beitreten importieren
entry.set_volume(0.07)                                      #Lautstärke minimieren
entry.play()                                                #sound einmal abspielen

mixer.music.load('Audio/backgroundmusic.mp3')
mixer.music.set_volume(0.015)
mixer.music.play(-1)                                        #sound auf Schleife abspielen

pause = 0                                                   #pause auf 0 setzen(wird für bulletcooldown gebraucht)


def player_movement(keys_pressed):                                  #player movement abhängig von parameter key_pressed
    player_RECT = pygame.Rect(player.X, player.Y, player.WIDTH, player.HEIGHT)
    if keys_pressed[pygame.K_a] and not ((player_RECT.midleft < cactus_RECT.midright and player_RECT.midright >= cactus_RECT.midleft) and player_RECT.centery >= cactus_RECT.centery-100):  # links wenn a gedrückt wird
        player.X -= player.X_VEL
        player.is_RUN_LEFT = True

    else:
        player.is_RUN_LEFT = False

    if keys_pressed[pygame.K_d] and not ((player_RECT.midright > cactus_RECT.midleft and player_RECT.midleft <= cactus_RECT.midright) and player_RECT.centery >= cactus_RECT.centery-100):  # rechts wenn d gedrückt wird
        player.X += player.X_VEL
        player.is_RUN_RIGHT = True

    else:
        player.is_RUN_RIGHT = False



def jumping_gravity(keys_pressed):
    if player.is_FALL:                                           # FALLING
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
    player_RECT = pygame.Rect(player.X, player.Y, player.WIDTH, player.HEIGHT)          #player bekommt Kordinaten die sich mit ihm verändern geht von oben links des spieler RECTS aus

    if player_RECT.bottom >= ground_RECT.top:
        player.is_FALL = False
    else:
        player.is_FALL = True

def shoot_right(keys_pressed, tick):                #schuss nach rechts
    global pause                    #pause in funktion einfügen
    if keys_pressed[pygame.K_RIGHT] and pause+60<=tick and not bullet.is_shoot_R and not bullet.is_shoot_L:             #wenn die rechte pfeiltaste gedrückt wird schießt er nach rechts
        pause = tick
        bullet.is_shoot_R = True
        bullet.x = player.X + player.WIDTH / 2 +30                          #startpunkt der Bullet auf x-Achse
        bullet.y = player.Y + player.HEIGHT / 2 -10                         ##startpunkt der Bullet auf y-Achse
        shot = pygame.mixer.Sound("Audio/shot.mp3")                         #audio wird abgespielt
        shot.set_volume(0.025)
        shot.play()
    if bullet.is_shoot_R:
        bullet.x += bullet.vel
        if (bullet.x >= 650 and bullet.y>=475) and not bullet.x >= 700 and bullet.y>=475:              #wenn die kugel den kaktus trifft ertönt sound und kugel wird auf y= -10 gestzet--bedeutet auserhalb des fensters
            bullet.is_shoot_R = False
            hitmarker = pygame.mixer.Sound("Audio/hitmarker.mp3")
            hitmarker.set_volume(0.025)
            hitmarker.play()
            bullet.y = -10

        if bullet.x > WIDTH:
            bullet.is_shoot_R = False


def shoot_left(keys_pressed, tick):
    global pause
    if keys_pressed[pygame.K_LEFT] and pause+60<=tick and not bullet.is_shoot_R and not bullet.is_shoot_L:
        pause = tick
        bullet.is_shoot_L = True
        bullet.x = player.X + player.WIDTH / 2 -30
        bullet.y = player.Y + player.HEIGHT / 2 -10
        shot = pygame.mixer.Sound("Audio/shot.mp3")
        shot.set_volume(0.025)
        shot.play()
    if bullet.is_shoot_L:
        bullet.x -= bullet.vel
        if (bullet.x <= 700 and bullet.y>=475) and not bullet.x <= 620 and bullet.y>=475:
            bullet.is_shoot_L = False
            hitmarker = pygame.mixer.Sound("Audio/hitmarker.mp3")
            hitmarker.set_volume(0.025)
            hitmarker.play()
            bullet.y = -10

        if bullet.x < -10:
            bullet.is_shoot_L = False




