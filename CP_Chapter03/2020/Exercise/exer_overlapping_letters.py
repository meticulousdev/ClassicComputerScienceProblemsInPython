# Exercise 3.8 - 1
# title   : Word search algorithm with overlapping letters
# version : 1.0 (2020.09.13)

from typing import NamedTuple, Tuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint

Grid = List[List[str]]


class GridLocation(NamedTuple):
    row: int
    column: int


def generate_grid(rows: int, columns: int) -> Grid:
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]


def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))


def generate_domain(word: str, grid: Grid) -> List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0])
    length: int = len(word)

    for row in range(height):
        for col in range(width):
            columns: range = range(col, col + length + 1)
            rows: range = range(row, row + length + 1)
            if col + length <= width:
                domain.append([GridLocation(row, c) for c in columns])
                if row + length <= height:
                    domain.append([GridLocation(r, col + (r - row)) for r in rows])
            if row + length <= height:
                domain.append([GridLocation(r, col) for r in rows])
                if col - length >= 0:
                    domain.append([GridLocation(r, col - (r - row)) for r in rows])
    return domain


# Datatype of variables was changed from List[str] to List[Tuple].
# Tuple is a hashable datatype which can be used to key of dictionary.
class WordSearchConstraint(Constraint[Tuple, List[GridLocation]]):
    def __init__(self, words: List[Tuple]) -> None:
        super().__init__(words)
        self.words: List[Tuple] = words

    def satisfied(self, assignment: Dict[Tuple, List[GridLocation]]) -> bool:
        all_locations = [locs for values in assignment.values() for locs in values]
        return len(set(all_locations)) == len(all_locations)


if __name__ == "__main__":
    grid: Grid = generate_grid(10, 10)
    words: List[Tuple] = [("PYTHON", 0), ("PYTHON", 1), ("PYTHON", 2), ("PYTHON", 3),
                          ("JAVA", 0), ("JAVA", 1),
                          ("MATLAB", 0), ("MATLAB", 1),
                          ("SWIFT", 0),
                          ("MYSQL", 0), ("MYSQL", 1)]
    locations: Dict[Tuple, List[List[GridLocation]]] = {}
    for word in words:
        locations[word] = generate_domain(word[0], grid)
    csp: CSP[Tuple, List[GridLocation]] = CSP(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution: Optional[Dict[str, List[GridLocation]]] = csp.backtracking_search()

    if solution is None:
        print("답을 찾을 수 없습니다.")
    else:
        for word, grid_locations in solution.items():
            if choice([True, False]):
                grid_locations.reverse()
            for index, letter in enumerate(word[0]):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter
        display_grid(grid)
