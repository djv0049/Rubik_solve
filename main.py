# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from src.builder import Builder


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
