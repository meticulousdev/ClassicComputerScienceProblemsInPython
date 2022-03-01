from csp import Constraint, CSP
from typing import Dict, List, Optional


class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        return assignment[self.place1] != assignment[self.place2]


if __name__ == "__main__":
    variables: List[str] = ["웨스턴 오스트레일리아", "노던 준주", "사우스 오스트레일리아",
                            "퀸즐랜드", "뉴사우스웨일스", "빅토리아", "태즈메이니아"]
    domains: Dict[str, List[str]] = {}

    for variable in variables:
        domains[variable] = ["빨강", "초록", "파랑"]

    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint(MapColoringConstraint("웨스턴 오스트레일리아", "노던 준주"))
    csp.add_constraint(MapColoringConstraint("웨스턴 오스트레일리아", "사우스 오스트레일리아"))
    csp.add_constraint(MapColoringConstraint("사우스 오스트레일리아", "노던 준주"))
    csp.add_constraint(MapColoringConstraint("퀸즐랜드", "노던 준주"))
    csp.add_constraint(MapColoringConstraint("퀸즐랜드", "사우스 오스트레일리아"))
    csp.add_constraint(MapColoringConstraint("퀸즐랜드", "뉴사우스웨일스"))
    csp.add_constraint(MapColoringConstraint("뉴사우스웨일스", "사우스 오스트레일리아"))
    csp.add_constraint(MapColoringConstraint("빅토리아", "사우스 오스트레일리아"))
    csp.add_constraint(MapColoringConstraint("빅토리아", "뉴사우스웨일스"))
    csp.add_constraint(MapColoringConstraint("빅토리아", "태즈메이니아"))

    solution: Optional[Dict[str, str]] = csp.backtracking_search()
    if solution is None:
        print("답이 없습니다!")
    else:
        print(solution)
