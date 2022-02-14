# Exercise 3.8 - 3

# 제약 충족 문제 해결 프레임워크를 이용하여
# 스도쿠 문제를 해결할 수 있는 프로그램을 작성하라.
from typing import NamedTuple, List, Dict, Tuple, Optional
from csp import CSP, Constraint

Sudoku = List[List[int]]


class SudokuLocation(NamedTuple):
    row: int
    column: int


def display_sudoku(sudoku: Sudoku) -> None:
    for row in range(0, 9):
        for col in range(0, 9):
            print("{} ".format(sudoku[row][col]), end="")
        print()


def number_of_variables(sudoku: Sudoku) -> Dict[int, int]:
    variable: Dict[int, int] = {idx: 0 for idx in range(1, 10)}
    height: int = len(sudoku)
    width: int = len(sudoku[0])

    for row in range(height):
        for col in range(width):
            for idx in range(1, 10):
                if sudoku[row][col] == idx:
                    variable[idx] += 1
                else:
                    continue

    for idx in range(1, 10):
        variable[idx] = 9 - variable[idx]

    return variable


def generate_domain(sudoku: Sudoku) -> List[List[SudokuLocation]]:
    domain: List[List[SudokuLocation]] = []
    height: int = len(sudoku)
    width: int = len(sudoku[0])

    for row in range(height):
        for col in range(width):
            if sudoku[row][col] == 0:
                domain.append([SudokuLocation(row, col)])

    return domain


def sudoku_solution(sudoku: Sudoku, numbers: List[Tuple],
                    solution: Dict[Tuple, List[SudokuLocation]]) -> Sudoku:
    for number in numbers:
        row = (solution[number])[0].row
        col = (solution[number])[0].column
        sudoku[row][col] = number[0]

    return sudoku


class LocationSearchConstraint(Constraint[Tuple, List[SudokuLocation]]):
    def __init__(self, numbers: List[Tuple]) -> None:
        super().__init__(numbers)
        self.numbers: List[Tuple] = numbers

    def satisfied(self, assignment: Dict[Tuple, List[SudokuLocation]]) -> bool:
        all_locations = [locs for values in assignment.values() for locs in values]
        return len(set(all_locations)) == len(all_locations)


if __name__ == "__main__":
    unsolved_sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                       [6, 0, 0, 1, 9, 5, 0, 0, 0],
                       [0, 9, 8, 0, 0, 0, 0, 6, 0],
                       [8, 0, 0, 0, 6, 0, 0, 0, 3],
                       [4, 0, 0, 8, 0, 3, 0, 0, 1],
                       [7, 0, 0, 0, 2, 0, 0, 0, 6],
                       [0, 6, 0, 0, 0, 0, 2, 8, 0],
                       [0, 0, 0, 4, 1, 9, 0, 0, 5],
                       [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    novs: Dict[int, int] = number_of_variables(unsolved_sudoku)
    locations: Dict[Tuple, List[List[SudokuLocation]]] = {}

    numbers: List[Tuple] = []
    for i in range(1, 10):
        for j in range(novs[i]):
            numbers.append((i, j))

    for number in numbers:
        locations[number] = generate_domain(unsolved_sudoku)

    csp: CSP[Tuple, List[SudokuLocation]] = CSP(numbers, locations)
    csp.add_constraint(LocationSearchConstraint(numbers))
    solution: Optional[Dict[Tuple, List[SudokuLocation]]] = csp.backtracking_search()

    if solution is None:
        print("답을 찾을 수 없습니다.")
    else:
        print("*unsolved sudoku")
        display_sudoku(unsolved_sudoku)
        print()

        print("*solved sudoku")
        solved_sudoku = sudoku_solution(unsolved_sudoku, numbers, solution)
        display_sudoku(solved_sudoku)

    print()
