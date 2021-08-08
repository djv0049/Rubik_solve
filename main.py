# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from enum import Enum
# constant positions. this is how we will determine the positions of the litlle cubes within the cube
white_face_positions = {0, 3, 6, 9, 12, 15, 18, 21, 24}
blue_face_positions = {0, 1, 2, 3, 4, 5, 6, 7, 8}
green_face_positions = {18, 19, 20, 21, 22, 23, 24, 25, 26}
red_face_positions = {6, 7, 8, 15, 16, 17, 24, 25, 26}
orange_face_positions = {0, 1, 2, 9, 10, 11, 18, 19, 20}
yellow_face_positions = {2, 5, 8, 11, 14, 17, 20, 23, 26}


"""
****************#*#****************
******* Rubik's Cube Solver *******
 ********************************
  ***** By Daniel van Hoof *****
****************#*#****************

             ______________________________
            /         /         /         /|
           /         /         /         / |
          /_________/_________/_________/  |
         /         /         /         /| /|
        /         /         /         / |/ |
       /_________/_________/_________/  /  |
      /         /         /         /| /| /|
     /         /         /         / |/ |/ |
    /_________/_________/_________/  /  /  | 
    |         |         |         | /| /| /
    |         |         |         |/ |/ |/
    |_________|_________|_________|  /  /
    |         |         |         | /| /
    |         |         |         |/ |/
    |_________|_________|_________|  /
    |         |         |         | /
    |         |         |         |/
    |_________|_________|_________|
    

    - Daniel 8/8/21

"""

class Colors(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    ORANGE = 5
    WHITE = 6


# super class for all cubies, defines the cubie pos and id(finished pos)
class Cubies:
    def __init__(self, id, position):
        self.sides = []
        self.id = id
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

# defines the colors / associated cubies on a particular face
class Face:
    def __init__(self):
        self.squares = []
        self.positions = []

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass

    def rotate_180(self):
        pass

    def set_colors(self, colors: list):
        self.squares = [c for c in colors]



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




class Builder:
    def build_finished_cube(self):
        c3 = Cube(3)
        for i in range(27):
            print(i)
            new_cube = "None"
            if i == 13:
                continue  # 13 is the center piece
            elif i % 2 == 1:
                new_cube = EdgeCubie(i,i)
            elif i in [4, 10, 12, 14, 16, 22]:
                new_cube = CenterCubie(i,i)
            elif i in [0, 2, 6, 8, 18, 20, 24, 26]:
                new_cube = CornerCubie(i, i)
            else:
                print("there's a number that shouldn't be here in the cube creation... or your math is wrong daniel.")
            c3.cubies.append(new_cube)
        print("done")
        print(str(c3))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    b = Builder()
    b.build_finished_cube()



    # cube_json = {{6,6,6,6,6,6}, {}}
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


"""
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    ORANGE = 5
    WHITE = 6"""
