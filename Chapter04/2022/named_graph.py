from typing import TypeVar, Generic, List, Tuple
from graph import Graph
from named_edge import NamedEdge

V = TypeVar('V')


class NamedGraph(Generic[V], Graph[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[NamedEdge]] = [[] for _ in vertices]

    def add_edge_by_indices(self, u: int, v: int, u_name: str, v_name: str) -> None:
        edge: NamedEdge = NamedEdge(u, v, u_name, v_name)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first: V, second: V, u_name: str, v_name: str) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v, u_name, v_name)

    def neighbors_for_index_with_names(self, index: int) -> List[Tuple[V, str]]:
        distance_tuples: List[Tuple[V, str]] = []
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.v_name))
        return distance_tuples

    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_names(i)}\n"
        return desc


if __name__ == "__main__":
    # test basic Graph construction
    # land - A, B, C, D
    # bridge - a, b, c, d, e, f, g
    graph_Konigsberg: NamedGraph[str] = NamedGraph(["A", "B", "C", "D",
                                                    "a", "b", "c", "d", "e", "f", "g"])

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

    print(graph_Konigsberg)
