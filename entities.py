import pygame

class Entity:
    def __init__(self, X_POS:int, Y_POS, WIDTH, HEIGHT, X_VEL, Y_VEL, JUMP_POW):
        self.X = X_POS
        self.Y = Y_POS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.RECT = pygame.Rect(X_POS, Y_POS, WIDTH, HEIGHT)

        self.X_VEL = X_VEL
        self.Y_VEL = Y_VEL
        self.JUMP_POW = JUMP_POW

        self.is_STAND = False
        self.is_RUN_LEFT = False
        self.is_RUN_RIGHT = False
        self.is_FALL = False

        self.ANIM_COUNT = 0

player = Entity(20, 20, 100, 200, 8, 0, 14)


class Projectile:
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = vel
        self.is_shoot_R = False
        self.is_shoot_L = False

bullet = Projectile(-10, -10, 8, 8, 20)