class Cube:
    def __init__(self, size: int):
        self.sides = []
        self.cubies = []
        self.size = size
        self.square_count = size*size*size
        # todo add sides in here with their relative cubies

    def set_sides(self):
        for i in range(6):
            #self.sides.append(Face())
            # need to set one side at a time
            pass

    def __str__(self):
        return_string = ""
        for cubie in self.cubies:
            return_string += str(cubie)
        return return_string