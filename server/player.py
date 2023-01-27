import entity, positing, random, world

#time after damage to start regening in ticks
regen_time = 20*5

#                                                                                    TODO größe einstellen
class Player(entity.Entity):
    last_damage:int = 0
    last_move_command:int = 0
    def __init__(self, name:str, team:int, world:world.World) -> None:
        accelerate_speed = 3
        max_mov_speed = 5
        self.max_health = 100
        self.regenerate_speed = 5
        self.name = name
        self.health = self.max_health
        self.team = team

        super().__init__(300,150, world, accelerate_speed, max_mov_speed)

    #spawning the entity in the world
    def spawn(self) -> None:
        worldspawn = self.world.get_spawn(self.team)
        x1,x2 = worldspawn.pos1.x,worldspawn.pos1.x
        spawn_x = random.randint(x1,x2)

        world_rec = self.world.get_world_collider(spawn_x)
        self.set_pos(world_rec.get_Pos().y-self.height, spawn_x)

    # facing right -> True
    def get_looking_dir(self) -> bool:
        if self.vec.x > 0:
            return True
        return False
    
    #gets where to shoot the bullet                         TODO wo der Kopf ist muss noch angepasst werden / Arm
    def get_head(self) -> positing.Pos:
        if self.get_looking_dir(): width = self.width
        else: width = 0
        return positing.Pos(self.pos.x + width, self.pos.y - self.height + self.height/7)

    def get_health(self) -> int:
        return self.health

    #damages the player
    def damage(self, amount:int) -> None:
        self.health -= amount
        self.last_damage = self.tick
        if self.health <= 0:
            self.remove()
    
    #regenerats health that is set
    def regenerate_health(self) -> None:
        if self.health < self.max_health:
            self.health += self.regenerate_speed
            if self.health > self.max_health:
                self.health = self.max_health
    
    def move(self, go_right:bool) -> None:
        if self.last_move_command < self.tick:
            if go_right: ac = self.accelerate_speed
            else: ac = -self.accelerate_speed
            self.vec.accelerate(ac,0)
            if self.vec.x > self.max_mov_speed:
                self.vec.x = self.max_mov_speed
                
            self.last_move_command = self.tick

    #gets called when the player does not press anything
    def not_move(self) -> None:
        if self.last_move_command < self.tick:
            x = self.smooth_damp(self.vec.x, self.accelerate_speed)
            self.vec.set_vector(x, self.vec.y)

            self.last_move_command = self.tick

    #makes that current var (acceleration) approaches 0
    @staticmethod
    def smooth_damp(current:int, smooth_speed:int) -> int:
        if current < 0 and current + smooth_speed < 0:
            return current + smooth_speed
        if current > 0 and current - smooth_speed > 0:
            return current - smooth_speed
        return 0

    def collid(self, vec: positing.Vector, object:positing.Rect) -> None:
        if self.world.overlap(self.get_rect().move(positing.Vector(vec.x,0)), object):
            self.vec.set_vector(0,self.vec.y)
        else:
            self.vec.set_vector(self.vec.x, 0)

    #gets called every tick to update the player/entity
    def update(self, tick:int) -> None:
        super().update(tick)

        if tick > self.last_damage + regen_time and  tick%60 == 0:
            self.regenerate_health()

if __name__ == "__main__":
    pass