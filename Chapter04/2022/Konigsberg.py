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
    # 
    def satisfied(self, assignment: Dict[str, str]) -> bool:
        test: Dict[str, str]
        return test


if __name__ == "__main__":
    # [1] Graph
    nodes: List[str] = ["A", "B", "C", "D"]
    bridges: List[str] = ["a", "b", "c", "d", "e", "f", "g"]

    graph_total: List[str] = nodes + bridges
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

    print("Konigsberg - Graph") 
    print(graph_Konigsberg)

    # [2] CSP
    # TODO variables & domains
    # variables가 nodes + bridges일 경우 도메인은?
    # variables: List[str] = nodes + bridges
    # domains: Dict[str, List[str]] = {}

    # for variable in variables:
    #     domains[variable] = ["???"]

    # variables가 nodes인 경우
    # domains는 노드에 연결된 bridges
    variables: List[str] = nodes
    domains: Dict[str, List[str]] = {}

    for i, node in enumerate(nodes):
        domains[node] = graph_Konigsberg.neighbors_for_index(i)

    print("Konigsberg - variables and domains") 
    print(variables)
    print(domains)