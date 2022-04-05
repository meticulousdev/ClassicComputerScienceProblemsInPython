# Exercise 3.8 - 1
# title   : Word search algorithm with overlapping letters
# version : 0.2 (2022.04.05)
# wrong solution
from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
import matplotlib.pyplot as plt

from csp import CSP, Constraint


plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams.update({'mathtext.default':  'default'})
plt.rcParams.update({'font.size': 20})

Grid = List[List[str]]


class GridLocation(NamedTuple):
    row: int
    column: int


def generate_grid(rows: int, columns: int) -> Grid:
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]


# def display_grid01(grid: Grid) -> None:
#     for row in grid:
#         print("".join(row))
def display_grid(grid: Grid):
    height: int = len(grid)
    width: int = len(grid[0])
    lb: GridLocation = GridLocation(0, 0)
    rb: GridLocation = GridLocation(width, 0)
    lt: GridLocation = GridLocation(0, height)

    plt.figure(figsize=(7, 7))
    for i in range(0, (height + 1)):
        plt.plot([lb.row, rb.row], [lb.column + i, rb.column + i], 'k', alpha=0)
        plt.plot([lb.row + i, lt.row + i], [lb.column, lt.column], 'k', alpha=0)
    
    for i in range(0, height):
        for j in range(0, width):
            num = grid[(width - 1) - j][i]
            plt.text(i + 0.4, j + 0.4, str(num))
    
    plt.axis('off')
    plt.show()


def generate_domain(word: str, grid: Grid) -> List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0])
    length: int = len(word)

    for row in range(height):
        for col in range(width):
            columns: range = range(col, col + length)
            rows: range = range(row, row + length)
            if col + length <= width:
                domain.append([GridLocation(row, c) for c in columns])
                if row + length <= height:
                    domain.append([GridLocation(r, col + (r - row)) for r in rows])
            if row + length <= height:
                domain.append([GridLocation(r, col) for r in rows])
                if col - length >= 0:
                    domain.append([GridLocation(r, col - (r - row)) for r in rows])
    return domain


class WordSearchConstraint(Constraint[str, List[GridLocation]]):
    def __init__(self, words: List[str]) -> None:
        super().__init__(words)
        self.words: List[str] = words

    def satisfied(self, assignment: Dict[str, List[GridLocation]]) -> bool:
        cnt = 0
        for key01 in assignment.keys():
            for key02 in assignment.keys():
                if key01 == key02:
                    continue
                
                for i, locs01 in enumerate(assignment[key01]):
                    for j, locs02 in enumerate(assignment[key02]):
                        if locs01 == locs02:
                            if key01[i] == key02[j]:
                                cnt += 1
                                continue
                            else:
                                return False

        return True


if __name__ == "__main__":
    grid: Grid = generate_grid(9, 9)
    words: List[str] = ["MATTHEW", "JOE", "MARY", "SARAH", "SALLY"]
    for i, word in enumerate(words):
        if choice([True, False]):
            words[i] = word[::-1]
    # words: List[str] = ["PYTHON", "MYSQL", "GOLANG", "JULIA", "JAVA", "MATLAB"]
    locations: Dict[str, List[List[GridLocation]]] = {}
    for word in words:
        locations[word] = generate_domain(word, grid)
    csp: CSP[str, List[GridLocation]] = CSP(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution: Optional[Dict[str, List[GridLocation]]] = csp.backtracking_search()

    if solution is None:
        print("답을 찾을 수 없습니다.")
    else:
        for word, grid_locations in solution.items():
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter
        display_grid(grid)
