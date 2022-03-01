# 제약 충족 문제 해결 프레임워크를 이용하여
# 스도쿠 문제를 해결할 수 있는 프로그램을 작성하라.
from typing import NamedTuple, List, Dict, Set, Tuple, Optional
import random
from CP_Chapter03.csp import CSP, Constraint

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


def generate_domain(number: Tuple, sudoku: Sudoku) -> List[List[SudokuLocation]]:
    domain: List[List[SudokuLocation]] = []
    height: int = len(sudoku)
    width: int = len(sudoku[0])
    invalid_domain: Set[SudokuLocation] = set()

    for row in range(height):
        for col in range(width):
            if sudoku[row][col] == number[0]:
                # 가로, 세로 위치
                for idx in range(0, 9):
                    invalid_domain.add(SudokuLocation(row, idx))
                    invalid_domain.add(SudokuLocation(idx, col))

                # 박스 내부
                if row < 3 and col < 3:
                    for row_in in range(0, 3):
                        for col_in in range(0, 3):
                            invalid_domain.add(SudokuLocation(row_in, col_in))

                elif row < 3 and col < 6:
                    for row_in in range(0, 3):
                        for col_in in range(3, 6):
                            invalid_domain.add(SudokuLocation(row_in, col_in))

                elif row < 3 and col < 9:
                    for row_in in range(0, 3):
                        for col_in in range(6, 9):
                            invalid_domain.add(SudokuLocation(row_in, col_in))

                elif row < 6 and col < 3:
                    for row_in in range(3, 6):
                        for col_in in range(0, 3):
                            invalid_domain.add(SudokuLocation(row_in, col_in))

                elif row < 6 and col < 6:
                    for row_in in range(3, 6):
                        for col_in in range(3, 6):
                            invalid_domain.add(SudokuLocation(row_in, col_in))

                elif row < 6 and col < 9:
                    for row_in in range(3, 6):
                        for col_in in range(6, 9):
                            invalid_domain.add(SudokuLocation(row_in, col_in))

                elif row < 9 and col < 3:
                    for row_in in range(6, 9):
                        for col_in in range(0, 3):
                            invalid_domain.add(SudokuLocation(row_in, col_in))

                elif row < 9 and col < 6:
                    for row_in in range(6, 9):
                        for col_in in range(3, 6):
                            invalid_domain.add(SudokuLocation(row_in, col_in))

                elif row < 9 and col < 9:
                    for row_in in range(6, 9):
                        for col_in in range(6, 9):
                            invalid_domain.add(SudokuLocation(row_in, col_in))

    for row in range(height):
        for col in range(width):
            if (sudoku[row][col] == 0) and (SudokuLocation(row, col) not in invalid_domain):
                domain.append([SudokuLocation(row, col)])

    return domain


def sudoku_solution(sudoku: Sudoku, numbers: List[Tuple],
                    solution: Dict[Tuple, List[SudokuLocation]]) -> Sudoku:
    for number in numbers:
        row = (solution[number])[0].row
        col = (solution[number])[0].column
        sudoku[row][col] = number[0]

    return sudoku


def sudoku_checker(sudoku1: Sudoku, sudoku2: Sudoku) -> Sudoku:
    height: int = len(sudoku1)
    width: int = len(sudoku1[0])
    sudoku: Sudoku = [[0 for _ in range(height)] for _ in range(width)]

    for row in range(height):
        for col in range(width):
            sudoku[row][col] = sudoku1[row][col] - sudoku2[row][col]

    return sudoku


class LocationSearchConstraint(Constraint[Tuple, List[SudokuLocation]]):
    def __init__(self, numbers: List[Tuple]) -> None:
        super().__init__(numbers)
        self.numbers: List[Tuple] = numbers

    def satisfied(self, assignment: Dict[Tuple, List[SudokuLocation]]) -> bool:
        all_locations = [locs for values in assignment.values() for locs in values]
        return len(set(all_locations)) == len(all_locations)


if __name__ == "__main__":
    solution_sudoku = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                       [6, 7, 2, 1, 9, 5, 3, 4, 8],
                       [1, 9, 8, 3, 4, 2, 5, 6, 7],
                       [8, 5, 9, 7, 6, 1, 4, 2, 3],
                       [4, 2, 6, 8, 5, 3, 7, 9, 1],
                       [7, 1, 3, 9, 2, 4, 8, 5, 6],
                       [9, 6, 1, 5, 3, 7, 2, 8, 4],
                       [2, 8, 7, 4, 1, 9, 6, 3, 5],
                       [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    # Sudoku generation
    height: int = len(solution_sudoku)
    width: int = len(solution_sudoku[0])
    solved_sudoku: Sudoku = [[0 for _ in range(width)] for _ in range(height)]
    unsolved_sudoku: Sudoku = [[0 for _ in range(width)] for _ in range(height)]

    for row in range(height):
        for col in range(width):
            unsolved_sudoku[row][col] = solution_sudoku[row][col]

    for _ in range(25):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        unsolved_sudoku[row][col] = 0

    # Solution search
    novs: Dict[int, int] = number_of_variables(unsolved_sudoku)
    locations: Dict[Tuple, List[List[SudokuLocation]]] = {}

    numbers: List[Tuple] = []
    for i in range(1, 10):
        for j in range(novs[i]):
            numbers.append((i, j))

    locations: Dict[Tuple, List[List[SudokuLocation]]] = {}
    for number in numbers:
        locations[number] = generate_domain(number, unsolved_sudoku)

    csp: CSP[Tuple, List[SudokuLocation]] = CSP(numbers, locations)
    csp.add_constraint(LocationSearchConstraint(numbers))
    solution: Optional[Dict[Tuple, List[SudokuLocation]]] = csp.backtracking_search()

    # Solution Check
    if solution is None:
        print("답을 찾을 수 없습니다.")
    else:
        print("number of zeros: {}".format(len(numbers)))
        print("*unsolved sudoku")
        display_sudoku(unsolved_sudoku)
        print()

        print("*solved sudoku")
        solved_sudoku = sudoku_solution(unsolved_sudoku, numbers, solution)
        display_sudoku(solved_sudoku)
        print()

        print("*solution check")
        display_sudoku(sudoku_checker(solution_sudoku, solved_sudoku))
        print()
