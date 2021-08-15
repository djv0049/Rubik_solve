from src.cube import Cube
from src.cubies import CenterCubie
from src.cubies import EdgeCubie
from src.cubies import CornerCubie
from src.side import Face
from src.colors import Colors
"""

potentially adhering to the builder pattern
this class will handle the initial construction of the cube
removing the responsibilities from the client code and creating abstraction.

"""

class Builder:
    @staticmethod
    def build_finished_cube():
        c3 = Cube(3)
        for i in range(27):
            # print(i)
            new_cube = "None"
            if i == 13:
                continue  # 13 is the center piece
            elif i % 2 == 1:
                new_cube = EdgeCubie(i, i)
            elif i in [4, 10, 12, 14, 16, 22]:
                new_cube = CenterCubie(i, i)
            elif i in [0, 2, 6, 8, 18, 20, 24, 26]:
                new_cube = CornerCubie(i, i)
            else:
                print("there's a number that shouldn't be here in the cube creation... or your math is wrong daniel.")
            c3.cubies.append(new_cube)
        c3.sides.append(Face(Colors.RED, Colors.RED))
        c3.sides.append(Face(Colors.ORANGE, Colors.ORANGE))
        c3.sides.append(Face(Colors.YELLOW, Colors.YELLOW))
        c3.sides.append(Face(Colors.GREEN, Colors.GREEN))
        c3.sides.append(Face(Colors.BLUE, Colors.BLUE))
        c3.sides.append(Face(Colors.WHITE, Colors.WHITE))
        # print(str(c3))
        print("done")
        return c3


