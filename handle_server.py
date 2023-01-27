import network, pickle, entities, draw_window

def recif():
    while True:
        msg = network.recif()
        try:
            pickeled_entity = pickle.loads(msg)
        except pickle.UnpicklingError:
            print(msg, type(msg))
            msg = msg.decode("utf-8")
            msg = msg.replace(" ", "")
            msg = bytes(msg, "utf-8")
            pickeled_entity = pickle.loads(msg)
        if isinstance(pickeled_entity, entities.Entity):
            draw_window.set_other_player(pickeled_entity)
        elif pickeled_entity:
            draw_window.other_bullets = pickeled_entity
            
def send_player():
    pickled_player = pickle.dumps(entities.player)
    network.send(pickled_player)
    if entities.bullet == None:
        pickled_bullet = pickle.dumps(entities.bullet)
        network.send(pickled_bullet)