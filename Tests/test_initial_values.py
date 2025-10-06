"""
for semi-test driven development, this will test the state of the cube on initial creation
ensuring default values are as expected
note: default cube === completed cube
"""

"""
Test default values - testing that the values in the cubie id field are the same as the position
Test  
"""
from unittest import TestCase
from src.builder import Builder


class TestClass(TestCase):
    def setUp(self):
        self.cube = Builder.build_finished_cube()

    default_cube = Builder.build_finished_cube()

    def test_default_values(self):
        assert self.cube.sides[0].positions[0] == 6

    def test_rotate_face_clockwise_changes_face(self):
        self.cube.rotate(self.cube.sides[0], 1)
        red_face = self.cube.sides[0].squares
        # assert:
        self.assertEqual(red_face, [24, 15, 6, 7, 8, 17, 26, 25, 16])


    def test_rotate_face_changes_surrounding_faces(self):
        self.cube.rotate(self.cube.sides[0], 1)
        red_face = self.cube.sides[0].squares
        yellow_face = self.cube.sides[2].squares
        green_face = self.cube.sides[3].squares
        blue_face = self.cube.sides[4].squares
        white_face = self.cube.sides[5].squares
        # assert:
        self.assertEqual(yellow_face, [6, 5, 2, 11, 20, 23, 8, 7, 14])
        self.assertEqual(blue_face, [0, 1, 2, 5, 4, 6, 15, 24, 3, 4])
        self.assertEqual(green_face, [20, 19, 18, 21, 26, 17, 8, 23, 22])
        self.assertEqual(white_face, [0, 3, 24, 25, 26, 21, 18, 9, 12])


    def test_short_algorithm(self):
        # R' B' R G R' B R G'
        # swaps three of the corners on the red face
        r = self.cube.sides[0]
        b = self.cube.sides[4]
        g = self.cube.sides[3]
        self.cube.rotate(r, -1)
        self.cube.rotate(b, -1)
        self.cube.rotate(r, 1)
        self.cube.rotate(g, 1)
        self.cube.rotate(r, -1)
        self.cube.rotate(b, 1)
        self.cube.rotate(r, 1)
        self.cube.rotate(g, -1)
        self.assertEqual(self.cube.sides[0].squares, [6, 7, 24, 17, 8, 25, 26, 15, 16])

    def test_repeated_algorithm_goes_back_to_start(self):
        # R' B' R G R' B R G'
        # swaps three of the corners on the red face
        r = self.cube.sides[0]
        b = self.cube.sides[4]
        g = self.cube.sides[3]
        for i in range(3):
            self.cube.rotate(r, -1)
            self.cube.rotate(b, -1)
            self.cube.rotate(r, 1)
            self.cube.rotate(g, 1)
            self.cube.rotate(r, -1)
            self.cube.rotate(b, 1)
            self.cube.rotate(r, 1)
            self.cube.rotate(g, -1)

        for side in default_cube.sides:
            index = default_cube.sides.index(side)
            tested_side = self.cube.sides[index]
            for square in side.squares:
                square_index = side.positions.index(square)
                tested_side_square = tested_side.positions[square_index]

                self.assertEqual(tested_side_square, square)
