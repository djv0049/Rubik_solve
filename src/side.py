
from src.colors import Colors
"""
|--------|--------------------------------------|
|  Face  | positions                            |
|--------|--------------------------------------|
| red    | 6, 7, 8, 15, 16, 17, 24, 25, 26      |
| orange | 0, 1, 2, 9, 10, 11, 18, 19, 20       |
| yellow | 2, 5, 8, 11, 14, 17, 20, 23, 26      |
| green  | 18, 19, 20, 21, 22, 23, 24, 25, 26   |
| blue   | 0, 1, 2, 3, 4, 5, 6, 7, 8            |
| White  | 0, 3, 6, 9, 12, 15,18, 21, 24        |
|--------|--------------------------------------|

"""
class Face:
    def __init__(self, color: Colors):  # color represents the middle square on the cube face
        self.squares = []
        self.positions = []
        self.set_positions(color)

    def rotate_anti_clockwise(self):
        pass

    def rotate_clockwise(self):
        pass

    def rotate_180(self):
        pass

    def set_colors(self, colors: list):
        self.squares = [c for c in colors]

    # TODO set up the arrays in a clockwise order with the last one being the center. (like a clockwise spiral)
    def set_positions(self, color: Colors):
        if color == Colors.RED:
            self.positions = [6, 7, 8, 15, 16, 17, 24, 25, 26]
        elif color == Colors.ORANGE:
            self.positions = [0, 1, 2, 9, 10, 11, 18, 19, 20]
        elif color == Colors.YELLOW:
            self.positions = [2, 5, 8, 11, 14, 17, 20, 23, 26]
        elif color == Colors.BLUE:
            self.positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        elif color == Colors.GREEN:
            self.positions = [18, 19, 20, 21, 22, 23, 24, 25, 26]
        elif color == Colors.WHITE:
            self.positions = [0, 3, 6, 9, 12, 15, 18, 21, 24]


