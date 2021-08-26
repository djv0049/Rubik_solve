from src.side import Face
from src.colors import Colors
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

    """rotates a side. enter the color of the side and 1 for clockwise, -1 for anticlockwise"""
    def rotate(self, side, direction:int):
        if direction == 1:
            side.rotate_clockwise()
            self.update_surrounding_sides(side)
        elif direction == -1:
            side.rotate_anti_clockwise()
            self.update_surrounding_sides(side)

    def update_surrounding_sides(self, side: Face):
        for pos in side.positions:
            # find the positions index on the face
            pos_index_on_face = side.positions.index(pos)
            # find the cubie at that position on the face
            cubie_at_pos = side.squares[pos_index_on_face]

            # find sides with that position
            for face in self.sides:
                if pos in face.positions:
                    # find the positions index on that side
                    pos_index_new_face = face.positions.index(pos)
                    # set the new position to have the cubie at that pos
                    face.squares[pos_index_new_face] = cubie_at_pos

    def update_cube_cubies(self):
        pass