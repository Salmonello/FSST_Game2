import pygame
from events import *
from draw_window import *
import handle_server
import threading

pygame.mixer.init()
pygame.init()

pygame.display.set_caption("FSST Game")
FPS = 60
clock = pygame.time.Clock()


def main():
    tick = 0
    win = False
    run = True
    thread = threading.Thread(target=handle_server.recif)
    try:
        thread.start()
    except ConnectionRefusedError:
        print("connection refused")
        input("")
    while run:
        tick+=1
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                run = False
        
        collision_detection()
        player_movement(keys_pressed)
        jumping_gravity(keys_pressed)
        if not win:
            draw_win()
        else:
            WinWindow()
        shoot_right(keys_pressed,tick)
        shoot_left(keys_pressed,tick)
        checkbullet_hit(bullet)
        if checkwin():
            win= True


        handle_server.send_player()




    pygame.quit()


if __name__ == "__main__":
    main()