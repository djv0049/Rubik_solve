
from src.colors import Colors
"""
insert documentation here

"""


class Face:
    def __init__(self, color: Colors, square_id_list):  # color represents the middle square on the cube face
        self.color = color
        self.squares = []
        self.positions = []
        self.set_positions(color)
        self.set_cubies(color) # todo get rid of this and make it set the cubies dynamically

    def rotate_anti_clockwise(self):
        new_positions = [None] * 9
        for current_index in range(len(self.squares)):
            new_index = current_index - 2  # add special case for 6/7
            if current_index == 8:  # center piece
                new_index = current_index
            elif new_index < 0:
                new_index += 8
            new_positions[new_index] = self.squares[current_index]
        self.squares = new_positions

    def rotate_clockwise(self):

        new_positions = [None] * 9
        for current_index in range(len(self.squares)):
            new_index = current_index + 2  # add special case for 6/7
            if current_index == 8:   # center piece
                new_index = current_index
            elif new_index > 7:
                new_index -= 8
            new_positions[new_index] = self.squares[current_index]
        self.squares = new_positions

    def rotate_180(self):
        pass

    def update_cubie_position(self):
        # [cubie.position = pos for cubie in self.squares]
        for cubie in self.squares:
            cubie.set_position(self.positions[self.squares.index(cubie)])

    def set_squares(self, square_id_list: list):
        for square_id in square_id_list:
            self.squares.append(square_id)

    def set_positions(self, color: Colors):
        if color == Colors.RED:
            self.positions = [6, 7, 8, 17, 26, 25, 24, 15, 16]
        elif color == Colors.ORANGE:
            self.positions = [2, 1, 0, 9, 18, 19, 20, 11, 10]
        elif color == Colors.YELLOW:
            self.positions = [8, 5, 2, 11, 20, 23, 26, 17, 14]
        elif color == Colors.BLUE:
            self.positions = [0, 1, 2, 5, 4, 8, 7, 6, 3, 4]
        elif color == Colors.GREEN:
            self.positions = [20, 19, 18, 21, 24, 25, 26, 23, 22]
        elif color == Colors.WHITE:
            self.positions = [0, 3, 6, 15, 24, 21, 18, 9, 12]

    # todo temporary method will switch up for a dynamic method for any input
    def set_cubies(self, color: Colors):
        if color == Colors.RED:
            self.squares = [6, 7, 8, 17, 26, 25, 24, 15, 16]
        elif color == Colors.ORANGE:
            self.squares = [2, 1, 0, 9, 18, 19, 20, 11, 10]
        elif color == Colors.YELLOW:
            self.squares = [8, 5, 2, 11, 20, 23, 26, 17, 14]
        elif color == Colors.BLUE:
            self.squares = [0, 1, 2, 5, 4, 8, 7, 6, 3, 4]
        elif color == Colors.GREEN:
            self.squares = [20, 19, 18, 21, 24, 25, 26, 23, 22]
        elif color == Colors.WHITE:
            self.squares = [0, 3, 6, 15, 24, 21, 18, 9, 12]
