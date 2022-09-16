from tkinter.messagebox import NO
from typing import TypeVar, List, Dict, Optional
from graph import Graph
from csp import Constraint, CSP


V = TypeVar('V')


class Konigsberg(Constraint[str, str]):
    # TODO __init__
    def __init__(self, lands: str, bridges: str) -> None:
        super().__init__([lands, bridges])
        self.lands: str = lands
        self.bridges: str = bridges

    # TODO satisfied
    def satisfied(self, assignment: Dict[str, str]) -> bool:
        test: Dict[str, str]
        return test


if __name__ == "__main__":
    lands: List[str] = ["A", "B", "C", "D"]
    bridges: List[str] = ["a", "b", "c", "d", "e", "f", "g"]

    # TODO variables & domains
    variables: List[str] = lands + bridges
    domains: Dict[str, List[str]] = {}

    for variable in variables:
        domains[variable] = ["???"]

    graph_total: List[str] = lands + bridges
    graph_Konigsberg: Graph[str] = Graph(graph_total)

    graph_Konigsberg.add_edge_by_vertices("A", "a")
    graph_Konigsberg.add_edge_by_vertices("A", "b")
    graph_Konigsberg.add_edge_by_vertices("A", "c")
    graph_Konigsberg.add_edge_by_vertices("A", "d")
    graph_Konigsberg.add_edge_by_vertices("A", "e")
    
    graph_Konigsberg.add_edge_by_vertices("B", "a")
    graph_Konigsberg.add_edge_by_vertices("B", "b")
    graph_Konigsberg.add_edge_by_vertices("B", "f")
    
    graph_Konigsberg.add_edge_by_vertices("C", "c")
    graph_Konigsberg.add_edge_by_vertices("C", "d")
    graph_Konigsberg.add_edge_by_vertices("C", "g")
    
    graph_Konigsberg.add_edge_by_vertices("D", "e")
    graph_Konigsberg.add_edge_by_vertices("D", "f")
    graph_Konigsberg.add_edge_by_vertices("D", "g")
    
    print(graph_Konigsberg)