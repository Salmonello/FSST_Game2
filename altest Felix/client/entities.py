
class Entity:
    def __init__(self, X_POS, Y_POS, WIDTH, HEIGHT, X_VEL, Y_VEL, JUMP_POW):
        self.X = X_POS
        self.Y = Y_POS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.X_VEL = X_VEL
        self.Y_VEL = Y_VEL
        self.JUMP_POW = JUMP_POW

        self.is_STAND = False
        self.is_RUN_LEFT = False
        self.is_RUN_RIGHT = False
        self.is_FALL = False

        self.ANIM_COUNT = 0

player = Entity(20, 20, 150, 300, 10, 0, 12)