# super class for all cubies, defines the cubie pos and id(finished pos)
class Cubies:
    def __init__(self, cubie_id, position):
        self.sides = []
        self.id = cubie_id
        self.position = position

    def get_sides(self):
        return self.sides

    def __str__(self):
        return_string = f'Id: {self.id} \nPosition: {self.position}\nSides:{self.sides}\n\n'
        return return_string


# corners, 3 faces/colors 8 positions and 3 orientations per pos
class CornerCubie(Cubies):
    def __init__(self, cube_id, position):
        super().__init__(cube_id, position)

    def set_sides(self, side1, side2, side3):
        self.sides.append(side1)
        self.sides.append(side2)
        self.sides.append(side3)


# bridges across 2 faces, has 2 colors, 12 positions with 2 orientations per pos
class EdgeCubie(Cubies):
    def __init__(self, cube_id, position):
        super().__init__(cube_id, position)

    def set_sides(self, side1, side2):
        self.sides.append(side1)
        self.sides.append(side2)


# has one face, does not move, defines the color of the face it's on
class CenterCubie(Cubies):
    def __init__(self, cube_id, position):
        super().__init__(cube_id, position)

    def set_sides(self, side1):
        self.sides.append(side1)