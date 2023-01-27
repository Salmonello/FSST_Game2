import network, game as gm, random
from player import *

clients = {int:network.Network}
in_game_clients = {int:network.PlayerData}
games = {int:gm.Game}

def get_command(msg:str) -> str:
    com = ""
    for i in range(4):
        com += msg[i]
    return str(com)

def get_msg(msg:str) -> list:
    msg_list = msg.split("/")
    msg_list.pop(0)
    return msg_list

def get_game(gamecode:int, net_id:int) -> gm.Game:
    game = games.get(gamecode, "")
    if game:
        return game
    else:
        return

def create_game(msg:str, net_id:int):
    game_code = random.randint(0,99999)
    name = get_msg(msg)[0]
    world = get_msg(msg)[1]
    client = clients.get(net_id)

    game = games.get(game_code, "")
    if not game:
        create_game(msg,client)

        game = gm.Game(game_code, world).set_admin(client.get_addr())
        client.send_client("info/opengame/" + str(game_code))

        join_game("join/" + str(game_code) + "/" + name + "/0")
        return
    create_game(msg, net_id)
    
def join_game(msg:str, net_id:int):
    msg = get_msg(msg)
    client = clients.get(net_id)
    gamecode = msg[0]
    name = msg[1]
    team = msg[2]
    
    game = get_game(gamecode, net_id)
    if game:
        player_data = network.PlayerData(client, name, team, game.world, gamecode)
        game.join(net_id,player_data)
        in_game_clients[net_id] = player_data
    else:
        client.send_client("erro/1")

def move(msg:str, net_id:int) -> None:
    move = get_msg(msg)[0]
    client = in_game_clients.get(net_id, "")
    if get_game(client.gamecode, net_id).has_started:
        client.get_player().move(move)
    else:
        client.net.send_client("erro/2")  

def not_move(msg:str, net_id:int) -> None:
    client = in_game_clients.get(net_id, "")
    if get_game(client.gamecode, net_id).has_started:
        client.get_player().not_move(move)
    else:
        client.net.send_client("erro/2")

def shoot(msg:str, net_id:int) -> None:
    client = in_game_clients.get(net_id, "")
    game = get_game(client.gamecode, net_id)
    if game.has_started:
        msg = get_msg(msg)
        game.shoot(client.get_player(), msg[0])
    else:
        client.net.send_client("erro/2")

def start_game(msg:str, net_id:int):
    msg = get_msg(msg)
    gamecode = msg[0]
    
    game = get_game(gamecode, net_id)
    if game:
        game.start_game(clients.get(net_id).get_addr())
    else:
        clients.get(net_id).send_client("erro/1")

commands = {"join": join_game, "crea": create_game, "move":move, "nomo": not_move, "shoo": shoot}

def set_network(net_id:int, net:network):
    clients[net_id] = net

def send_error(msg:str, net_id:int) -> None:
    clients.get(net_id).send_client("erro/0")

def handle_commands(msg:str, net_id:int):
    commands.get(get_command(msg), send_error)(msg, net_id)    

if __name__ == "__main__":

    handle_commands("creaast/12/felix",1)