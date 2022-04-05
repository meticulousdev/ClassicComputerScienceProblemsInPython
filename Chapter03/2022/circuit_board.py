# Exercise 3.8 - 2
# title   : Closed circuit design
# version : 0.2 (2022.04.03)
# author  : kobong
from typing import NamedTuple, Tuple, List, Dict, Optional
import random

from csp import CSP, Constraint

Grid = List[List[str]]


class GridLocation(NamedTuple):
    row: int
    column: int


def generate_grid(rows: int, columns: int) -> Grid:
    return [[" " for _ in range(columns)] for _ in range(rows)]


def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))


def display_chip(chip: Tuple[Tuple, Tuple]) -> None:
    chip_height: int = len(chip)
    chip_width: int = len(chip[0])

    for row in range(chip_height):
        for col in range(chip_width):
            print(chip[row][col], end="")
        print()


def generate_domain(chip: Tuple[Tuple, Tuple], grid: Grid) -> List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    # grid size
    height: int = len(grid)
    width: int = len(grid[0])
    # chip size
    chip_height: int = len(chip)
    chip_width: int = len(chip[0])

    for row in range(height):
        for col in range(width):
            columns_00: range = range(col, col + chip_width)
            rows_00: range = range(row, row + chip_height)
            columns_90: range = range(col, col + chip_height)
            rows_90: range = range(row, row + chip_width)

            # degree of chip rotation: 0 degree
            if (row + chip_height <= height) and (col + chip_width <= width):
                domain.append([GridLocation(r, c) for r in rows_00 for c in columns_00])
            # degree of chip rotation: 90 degree
            if (row + chip_width <= height) and (col + chip_height <= width):
                domain.append([GridLocation(r, c) for r in rows_90 for c in columns_90])

    return domain


class ChipSearchConstraint(Constraint[Tuple[Tuple, Tuple], List[GridLocation]]):
    def __init__(self, chips: List[Tuple[Tuple, Tuple]]) -> None:
        super().__init__(chips)
        self.chips: List[Tuple[Tuple, Tuple]]

    def satisfied(self, assignment: Dict[Tuple[Tuple, Tuple], List[GridLocation]]) -> bool:
        all_locations = [locs for values in assignment.values() for locs in values]
        return len(set(all_locations)) == len(all_locations)


if __name__ == "__main__":
    # grid generation
    grid: Grid = generate_grid(9, 9)

    # chip generation and assignment

    # case 1
    chips: List[Tuple[Tuple, Tuple]] = [
                                        # chip A
                                        (("A", "A", "A", "A", "A", "A")),
                                        # chip B
                                        (("B", "B", "B", "B"),
                                         ("B", "B", "B", "B")),
                                        # chip C
                                        (("C", "C", "C"),
                                         ("C", "C", "C"),
                                         ("C", "C", "C")),
                                        # chip D
                                        (("D", "D"),
                                         ("D", "D")),
                                        # chip E
                                        (("E", "E", "E", "E", "E"),
                                         ("E", "E", "E", "E", "E"))]

    # random case
    # chips: List[Tuple[Tuple, Tuple]] = []
    # candidate: List[str] = ["A", "B", "C", "D", "E"]
    # for i in range(5):
    #     row = random.randint(1, 5)
    #     col = random.randint(1, 5)
    #     temp: Tuple = tuple(candidate[i] for _ in range(col))

    #     chip: Tuple = ()
    #     for j in range(row):
    #         chip = (*chip, temp)

    #     print("chip {}".format(candidate[i]))
    #     display_chip(chip)
    #     chips.append(chip)
    #     print()

    # location assignment
    locations: Dict[Tuple[Tuple, Tuple], List[List[GridLocation]]] = {}
    for chip in chips:
        locations[chip] = generate_domain(chip, grid)

    # CSP
    csp: CSP[Tuple[Tuple, Tuple], List[GridLocation]] = CSP(chips, locations)
    csp.add_constraint(ChipSearchConstraint(chips))
    solution: Optional[Dict[str, List[GridLocation]]] = csp.backtracking_search()

    if solution is None:
        print("답을 찾을 수 없습니다.")
    else:
        for chip, grid_locations in solution.items():
            chip_height: int = len(chip)
            chip_width: int = len(chip[0])
            length = chip_height * chip_width

            for index in range(length):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = chip[0][0]
        display_grid(grid)
        print()
