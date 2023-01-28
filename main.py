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
    run = True
    thread = threading.Thread(target=handle_server.recif)
    try:
        thread.start()
    except ConnectionRefusedError:
        print("connection refused")
        input("")
    while run:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                run = False
        
        collision_detection()
        player_movement(keys_pressed)
        jumping_gravity(keys_pressed)
        draw_win()
        shoot_right(keys_pressed)
        shoot_left(keys_pressed)
        checkbullet_hit(other_player, bullet)
        checkbullet_gothit(player, other_bullets)

        handle_server.send_player()

    pygame.quit()


if __name__ == "__main__":
    main()