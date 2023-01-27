import pygame
from events import *
from draw_window import *
from camera import *

pygame.init()


pygame.display.set_caption("FSST Game")
FPS = 60
clock = pygame.time.Clock()


def main():
    run = True
    while run:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                run = False
        
        camera.cam_update()
        player_movement(keys_pressed)
        jumping_gravity(keys_pressed)
        draw_win()

    pygame.quit()


if __name__ == "__main__":
    main()