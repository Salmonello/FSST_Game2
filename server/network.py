import socket, world, player

HEADER = 32

# to send messages
class Network:
    def __init__(self, conn: socket.socket, addr: tuple) -> None:
        self.conn = conn
        self.addr = addr
    
    def send_client(self, msg:str) -> None:
        msg += b' ' * (HEADER - len(msg))
        self.conn.send(msg)
    
    def get_addr(self) -> tuple:
        return self.addr

    @staticmethod
    def send_to_all(clients:dict, msg:str) -> None:
        for client in clients:
            clients[client].send_client(msg)

# playerdata connects the server part of the game with the actual logic part
class PlayerData:
    def __init__(self, net:Network, name:str, team:int, world:world.World, gamecode:int) -> None:
        self.net = net
        self.gamecode = gamecode
        self.player = player.Player(name, team, world)
        
    def get_player(self) -> player.Player:
        return self.player

if __name__ == "__main__":
    players = PlayerData(1,"felix", 1, "baum")