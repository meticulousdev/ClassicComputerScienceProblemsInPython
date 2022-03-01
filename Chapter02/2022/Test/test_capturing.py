from typing import NamedTuple, Callable
from math import sqrt


class MazeLocation(NamedTuple):
    row: int
    column: int

    def __repr__(self):
        return f"({self.row}, {self.column})"


# TODO: fist class function & capturing
def euclidean_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        xdist: int = ml.column - goal.column
        ydist: int = ml.row - goal.row
        return sqrt((xdist * xdist) + (ydist * ydist))
    return distance
# end of euclidean_distance


if __name__ == "__main__":
    goal: MazeLocation = MazeLocation(10, 10)
    distance: Callable[[MazeLocation], float] = euclidean_distance(goal)

    current: MazeLocation = MazeLocation(0, 0)
    print(f"distance from current {current} to goal {goal}: {distance(current)}")

    current: MazeLocation = MazeLocation(1, 1)
    print(f"distance from current {current} to goal {goal}: {distance(current)}")