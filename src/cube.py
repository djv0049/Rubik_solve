from src.side import Face
from src.colors import Colors as c
class Cube:
    def __init__(self, size: int):
        self.sides = []
        self.cubies = []
        self.size = size
        self.square_count = size*size*size
        # self.set_up_sides()
        # todo add sides in here with their relative cubies

    # def set_up_sides(self):
    #     self.sides.append(Face(c.RED, f.RED))
    #     self.sides.append(Face(c.ORANGE, f.ORANGE))
    #     self.sides.append(Face(c.YELLOW, f.YELLOW))
    #     self.sides.append(Face(c.BLUE, f.BLUE))
    #     self.sides.append(Face(c.GREEN, f.GREEN))
    #     self.sides.append(Face(c.WHITE, f.WHITE))

    def get_sides(self):
        return self.sides

    def __str__(self):
        return_string = ""
        for cubie in self.cubies:
            return_string += str(cubie)
        return return_string