from positing import *
import world

GRAVITY = 5

class Entity:
    #sets all to 0 to avoid errors
    health:int
    has_gravity:bool = True
    is_falling:bool = False
    vec:Vector = Vector(0,0)
    gravity:bool = True
    pos = Pos(0,0)

    def __init__(self, height:int, width:int,  world:world.World, accelerate_speed:int, max_mov_speed:int) -> None:
        self.accelerate_speed = accelerate_speed
        self.max_mov_speed = max_mov_speed
        self.world = world

        self.width = width
        self.height = height

    #sets the postion of the entity by creating new rectiangls
    def set_pos(self, x:int ,y:int) -> None:
        self.pos = Pos(x,y)
        self.entity_rect = Rect(self.pos, self.pos.move_point(self.width, self.height))

    # gets the rect of the entity
    def get_rect(self) -> Rect:
        return self.entity_rect

    # sets if the entity falls
    def set_gravity(self, gravity:bool) -> None:
        self.gravity = gravity
    
    # callcalate the falling
    def fall(self) -> None:
        loaded_world = self.world.get_world_collider(self.pos)
        if not world.world.overlap(self.entity_rect, loaded_world): # FALLING 
            self.vec.accelerate(0,-self.gravity)
            self.is_falling = True
        else:
            self.vec.set_vector(self.vec.x,0)
            self.is_falling = False

    # updates the entity position so it starts moving
    def update_pos(self):
        moved_rect = self.get_rect().move(self.vec)
        world_collider = self.world.get_world_collider(self.pos)
        entity_collider = self.world.overlap_entity(moved_rect)

        if self.world.overlap(self.get_rect().move(self.vec), world_collider):
            self.collid(self.vec, world_collider)
        if entity_collider:
            self.collid(self.vec, entity_collider.get_rect())

        #moves the player finaly
        self.pos = self.get_rect().move(self.vec.x,self.vec.y).get_Pos()

    # gets called when it collides
    def collid(self, vec:Vector, object: Rect) -> None:
        pass

    # sets the entity movement to a specific vallue
    def set_movement(self, vec:Vector) -> None:
        self.vec.set_vector(vec.x,vec.y)

    #gets called every tick to callcalate everything
    def update(self, tick:int) -> None:                                                             #TODO wenn man das spiel startet könnte es sein das sich die spieler positionen nicht updaten aber versuchen es wird warscheinlich funktionieren
        self.fall()
        self.update_pos()

        # gets called when the player leaves the playable zone
        if not self.world.overlap(self.get_rect(), self.world.not_death):
            self.remove()

        self.tick = tick

    # gets called when dies
    def remove(self) -> None:
        self.world.remove_entity(self)