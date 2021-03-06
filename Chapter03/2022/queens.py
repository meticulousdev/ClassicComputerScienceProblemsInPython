from csp import Constraint, CSP
from typing import List, Dict, Optional


class QueensConstraint(Constraint[int, int]):
    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns: List[int] = columns

    def satisfied(self, assignment: Dict[int, int]) -> bool:
        for q1c, q1r in assignment.items():
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]
                    if q1r == q2r:
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):
                        return False
        return True


def display_queens(solution: Dict[int, int]) -> None:
    for i in range(1, 9):
        for j in range(1, 9):
            print("■" if solution[i] == j else '□', end="")
        print()
    print()



if __name__ == "__main__":
    for i in range(3, 9):
        columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
        rows: Dict[int, List[int]] = {}

        # for column in columns:
        #     rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
        rows[1] = [1]
        rows[2] = [i]
        rows[3] = [1, 2, 3, 4, 5, 6, 7, 8]
        rows[4] = [1, 2, 3, 4, 5, 6, 7, 8]
        rows[5] = [1, 2, 3, 4, 5, 6, 7, 8]
        rows[6] = [1, 2, 3, 4, 5, 6, 7, 8]
        rows[7] = [1, 2, 3, 4, 5, 6, 7, 8]
        rows[8] = [1, 2, 3, 4, 5, 6, 7, 8]

        # csp: CSP[int, int] = CSP(variables, domains)
        csp: CSP[int, int] = CSP(columns, rows)

        csp.add_constraint(QueensConstraint(columns))
        # 답이 1가지만 나오나?
        solution: Optional[Dict[int, int]] = csp.backtracking_search()

        if solution is None:
            print("답을 찾을 수 없습니다!")
        else:
            print(solution)
            display_queens(solution)
