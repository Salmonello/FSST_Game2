from entities import *
from load_image import *

class Cam:
    def __init__(self):
        self.POS_X = 0
        self.POS_Y = 0  
        
    def cam_update():
        camera.POS_X = (player.X - WIDTH/2)
        camera.POS_Y = (player.Y - HEIGHT/2)

camera = Cam