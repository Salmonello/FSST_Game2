import numpy

#for storing all of the positions
class Pos:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
    
    # returns himself to a position and returns that point
    def move_point(self, x:int, y:int):
        return Pos(self.x + x, self.y + y)

    # looks if a point overlaps with an rect
    def overlap(self, rect) -> bool:
        if rect.pos1.x < self.x and rect.pos2.x > self.x and rect.pos1.y < self.y and rect.pos2.y > self.y:
            return True
        return False

    #so it returns a nice string
    def __str__(self) -> str:
        return ('0' * (8  - len(str(round(self.x,3))))) + str(round(self.x, 3)) + "/" + ('0' * (8  - len(str(round(self.y, 3))))) + str(round(self.y, 3))

#stores a cube based of two positions
#so this can not be moved
class Rect:
    pos1:Pos
    pos2:Pos

    def __init__(self, pos1:Pos, pos2:Pos) -> None:
        self.pos1 = pos1
        self.pos2 = pos2

    #gets the size of the cube
    def get_size(self) -> int:
        return (self.pos1.x - self.pos2.x) * (self.pos1.y - self.pos2.y)
    
    #gets the position of the cube
    def get_Pos(self) -> Pos:
        return self.pos1

    #returns a moved rect
    def move(self, vec):
        return Rect(self.pos1.move_point(vec.x, vec.y), self.pos2.move_point(vec.x, vec.y))


#vector how much something will move
class Vector:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

    #accelerates the point and normalize
    def accelerate(self, x_mov, y_mov) -> None:
        self.x += x_mov
        self.y += y_mov

    #gets the vector length
    def get_vector(self) -> int:
        return numpy.sqrt(self.x*self.x + self.y*self.y)

    #sets the vector length between 0 and 1
    def normalize(self):
        if self.get_vector() > 0.1:
            length = numpy.sqrt(self.x**2 + self.y**2)
            self.x = self.x/length
            self.y = self.y/length
        return self

    #sets the vector to a specific vector
    def set_vector(self,x,y):
        self.x = x
        self.y = y
        return self

    #sets the vec to a specific angel
    def set_angel_movement(self, angel:int) -> None:
        angel = numpy.radians(angel)
        self.x = numpy.cos(angel+90)
        self.y = numpy.sin(angel+90)

    #returns a nice string when the 
    def __str__(self) -> str:
        return ('0' * (8  - len(str(round(self.x,3))))) + str(round(self.x, 3)) + "/" + ('0' * (8  - len(str(round(self.y, 3))))) + str(round(self.y, 3))

if __name__ == "__main__":
    pos = Pos(2345.1234,0.20384)
    print(pos)
    print(len(pos.__str__()))