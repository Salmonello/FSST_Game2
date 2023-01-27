from entity import *
import positing as po, player

class Bullet(Entity):
    damage = 50

    def __init__(self, world: world.World, pos: Pos) -> None:
        length = 10
        height = 2

        accelerate_speed = 5
        max_mov_speed = 10

        super().__init__(length, height, world, accelerate_speed, max_mov_speed)

        self.set_pos(pos.x,pos.y)

    #changes the super method so the bullet gets removed
    def collid(self, vec:Vector, object) -> None:
        if isinstance(object, player.Player):
            object.damage(self.damage)
        else:
            self.remove()

    #shoots the bullet at a specific angel
    def shoot(self, angel):
        self.vec.set_angel_movement(angel)
        return self