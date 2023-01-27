from network import *
import pygame, multiprocessing, player, world, bullet

class Game:
    clients = {int:PlayerData}
    tick = 0
    server_tick_speed:int

    def __init__(self, gamecode:int, world:world.World) -> None:
        self.gamecode = gamecode
        self.world = world
        self.has_started = False
        self.shoot_cool_down = 0

    def set_admin(self, admin:tuple) -> None:
        self.admin = admin

    def join(self, net_id:int, client:PlayerData) -> None:
        self.clients[net_id] = client
        Network.send_to_all(self.clients,"plaj/" + client.get_player().name + "/" + str(net_id))

    def start_game(self, admin:tuple) -> None:
        if self.admin == admin:
            self.has_started = True
            Network.send_to_all(self.clients, "info/start")

            for client in self.clients:
                self.clients.get(client).get_player().spawn()
            
            self.loop = multiprocessing.Process(target=self.game_loop)
            self.loop.start()   

    def game_loop(self) -> None:
        clock = pygame.time.Clock()
        while True:
            self.tick += 1

            for entiti in self.world.get_entities():
                entiti.update(self.tick)
                entity_type = "b"

                if isinstance(entiti, player.Player):
                    entity_type = "p"
                    # send all health to client
                    msg = "heal/" + str(entiti.health)
                    Network.send_to_all(self.clients, '0' * (3 -len(msg)) + str(msg))

                #send all pos to client
                msg = "pos" + entity_type + "/" + entiti.pos
                Network.send_to_all(self.clients, msg)
                
                # send all vel to clients
                msg = "vel" + entity_type + "/" + entiti.vec
                Network.send_to_all(self.clients, msg)
            
            clock.tick(20)
            self.server_tick_speed = clock.get_fps()
            print(self.server_tick_speed)

    #runns the inputet commands with the args as with the player_id
    def execute_comand(self, player_id:int, command, *args) -> None:
        command(self.clients[player_id], *args)

    #shoots out a bullet with given angel and vel
    def shoot(self, player:player.Player, angel:int) -> None:
        if self.shoot_cool_down + 10 < self.tick:
            entity = bullet.Bullet(self.world,player.get_head())
            entity.shoot(angel)
            self.world.add_entity(entity)
            self.shoot_cool_down = self.tick

if __name__ == "__main__":
    game = Game(12345)
    game.set_admin((12))
    game.start_game((12))

    Network("asd", (12,12)).send_to_all