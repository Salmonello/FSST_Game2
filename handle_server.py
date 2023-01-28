import network, pickle, entities, draw_window
            
def recif():
    while True:
        try:
            msg = network.recif()
            pickeled_entity = pickle.loads(msg)
        except:
            pass
        if isinstance(pickeled_entity, entities.Entity):
            draw_window.set_other_player(pickeled_entity)
        else:
            draw_window.set_other_bullets(pickeled_entity)
            
def send_player():
    pickled_player = pickle.dumps(entities.player)
    network.send(pickled_player)

    pickled_bullet = pickle.dumps(entities.bullet)
    if pickled_bullet:
        network.send(pickled_bullet)