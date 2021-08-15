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

class Test_test_class(TestCase):
    def before_all(self):

        pass

    def test_default_values(self):
        cube = Builder.build_finished_cube()
        assert cube.sides[0].positions[0] == 6

    def test_rotate_top_clockwise(self):
        # arrange
        cube = Builder.build_finished_cube()
        # act:
        cube.sides[0].rotate_clockwise()
        # assert:
        try:
            #assert cube.get_cubie_at(6).id == 24
            assert cube.sides[0].squares[0] == 24
            assert cube.sides[0].squares[1] == 15
            assert cube.sides[0].squares[2] == 6
        except AssertionError as e:
            res = "\n Expected {} to be {}, but got {} instead".format("cube", 24, cube.cubies[0].id)
            print(str(e) + res)

        pass
