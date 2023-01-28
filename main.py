import pygame
from events import *
from draw_window import *
import handle_server
import threading

pygame.mixer.init()                 #mixer für audio initieren
pygame.init()

pygame.display.set_caption("FSST Game")             #fenster name
FPS = 60                                            #tick speed
clock = pygame.time.Clock()                         #clock ist eine klasse um die ticks konstant zu halten


def main():
    tick = 0                            #tick auf null setzen
    win = False                         #wird bei sieg auf True gesetzt
    run = True                          #solang fenster läuft true
    thread = threading.Thread(target=handle_server.recife)
    thread.start()                                                      #server entpfängt Antwort von client
    while run:
        tick+=1                                                         #ticks erhöht sich mit verlauf solang spiel läuft
        clock.tick(FPS)                                                 #konstant 60 ticks gehalten
        keys_pressed = pygame.key.get_pressed()                         #keyboard input

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:          #spiel vrlassen
                run = False
        
        collision_detection()
        player_movement(keys_pressed)
        jumping_gravity(keys_pressed)
        if not win:
            draw_win()                          #fenster darstellen
        else:
            WinWindow()                            #sieger window darstellen
        shoot_right(keys_pressed,tick)
        shoot_left(keys_pressed,tick)
        checkbullet_hit(bullet)
        if checkwin():
            win= True


        handle_server.send_player()




    pygame.quit()


if __name__ == "__main__":
    main()