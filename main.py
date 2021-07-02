# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from enum import Enum


class Colors(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    ORANGE = 5
    WHITE = 6


class Cubies:
    def __init__(self):
        self.sides = []

    def get_sides(self):
        return self.sides


class CornerCubie(Cubies):
    def __init__(self, side1: int, side2: int, side3: int):
        super().__init__()
        self.sides.append(side1)
        self.sides.append(side2)
        self.sides.append(side3)


class EdgeCubie(Cubies):
    def __init__(self, side1: int, side2: int):
        super().__init__()
        self.sides.append(side1)
        self.sides.append(side2)


class CenterCubie(Cubies):
    super().__init__()
    def __init__(self, side1: int):
        self.sides.append(side1)


class Side:
    def __init__(self):
        self.squares = []

    def rotate_left(self):
        pass
    def rotate_right(self):
        pass
    def rotate_180(self):
        pass

    def set_colors(self, colors: list):
        self.squares = [c for c in colors]


class Layer:
    def __init__(self):
        self.cubies = []


class Cube:
    def __init__(self, size: int):
        self.sides = []
        self.cubies = []
        self.size = size
        self.square_count = size*size*size





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cube = Cube(2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
