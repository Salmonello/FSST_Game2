from positing import *
import json, os

class World():
    # where the player can spawn
    spawns = {}
    world_colliders:list = []

    #where the player is not killed
    #so the player does not fall in the void
    not_death = []

    entities = []

    # loads the world into the local variables
    def load_world(self, world_name) -> None:
        with open(os.path.join('server','worlds', world_name + '.json')) as file:
            data = json.load(file)
        
        death = data["not_death"]
        spawns = data["spawns"]
        colliders = data["collider"]

        self.not_death = Rect(Pos(death[0], death[1]), Pos(death[2], death[3]))

        for spawn in spawns:
            rec = spawns[spawn]
            self.spawns[spawn] = Rect(Pos(rec[0], 0), Pos(rec[1],0))

        for collider in colliders:
            for rectangle in colliders[collider]:
                rect = Rect(Pos(rectangle[0], 0), Pos(rectangle[2],0))
                self.world_colliders.append(rect)

    def get_spawn(self, spawn:int) -> Rect:
        return self.spawns.get(spawn, Rect(Pos(0,0),Pos(0,0)))

    # gets the rect on a specific position
    def get_world_collider(self,pos:Pos) -> Rect:
        for collider in self.world_colliders:
            if collider.pos1.x < pos.x and pos.x < collider.pos2.x:
                return collider

    #get the entity on a specific position
    #returns the entity
    def overlap_entity(self, rect:Rect):
        for entity in self.entities:
            if self.overlap(rect, entity.get_rect()):
                return entity
        return None

    # returns the entity list
    def get_entities(self) -> list:
        return self.entities

    # adds an entity
    def add_entity(self, entity) -> list:
        self.entities.append(entity)
        return self.entities

    #removes an entity
    def remove_entity(self, entity) -> None:
        self.entities.remove(entity)

    # looks if two rect overlap each other
    @staticmethod
    def overlap(obj1: Rect, obj2: Rect) -> bool:
        if obj1.pos1.x < obj2.pos2.x and obj1.pos2.x > obj2.pos1.x and obj1.pos1.y < obj2.pos2.y and obj1.pos2.y > obj2.pos1.y:
            return True
        return False

if __name__ == "__main__":
    world = World()
    world.load_world("world0")
    print(world.get_world_collider(Pos(50,100)))
    print(world.overlap(world.world_colliders[0], world.world_colliders[1]))
    print(world.spawns)