from tkinter.messagebox import NO
from typing import TypeVar, List, Optional
from named_graph import NamedGraph
from named_edge import NamedEdge

from generic_search import Stack, Queue


V = TypeVar('V')
NamedPath = List[NamedEdge]


def eulerian_trail(ng: NamedGraph[V], vi: List[str], start: int = 0) -> Optional[NamedPath]:
    # bfs dfs
    result = 1
    return result


def print_named_path(ng: NamedGraph, np: NamedPath) -> None:
    for edge in np:
        print(f"{ng.vertex_at(edge.u)} {edge.u_name} > {ng.vertex_at(edge.v)} {edge.v_name}")


if __name__ == "__main__":
    graph_Konigsberg: NamedGraph[str] = NamedGraph(["A", "B", "C", "D",
                                                    "a", "b", "c", "d", "e", "f", "g"])
    vertice_info: List[str] = ["land", "land", "land", "land",
                               "bridge", "bridge", "bridge", "bridge", 
                               "bridge", "bridge", "bridge"]

    graph_Konigsberg.add_edge_by_vertices("A", "a", "land", "bridge")
    graph_Konigsberg.add_edge_by_vertices("A", "b", "land", "bridge")
    graph_Konigsberg.add_edge_by_vertices("A", "c", "land", "bridge")
    graph_Konigsberg.add_edge_by_vertices("A", "d", "land", "bridge")
    graph_Konigsberg.add_edge_by_vertices("A", "e", "land", "bridge")
    
    graph_Konigsberg.add_edge_by_vertices("B", "a", "land", "bridge")
    graph_Konigsberg.add_edge_by_vertices("B", "b", "land", "bridge")
    graph_Konigsberg.add_edge_by_vertices("B", "f", "land", "bridge")
    
    graph_Konigsberg.add_edge_by_vertices("C", "c", "land", "bridge")
    graph_Konigsberg.add_edge_by_vertices("C", "d", "land", "bridge")
    graph_Konigsberg.add_edge_by_vertices("C", "g", "land", "bridge")
    
    graph_Konigsberg.add_edge_by_vertices("D", "e", "land", "bridge")
    graph_Konigsberg.add_edge_by_vertices("D", "f", "land", "bridge")
    graph_Konigsberg.add_edge_by_vertices("D", "g", "land", "bridge")
