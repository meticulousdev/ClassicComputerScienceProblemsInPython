from tkinter import W
from tkinter.messagebox import NO
from typing import TypeVar, List, Optional
from weighted_edge import WeightedEdge
from weighted_graph import WeightedGraph
from mst import mst, print_weighted_path


V = TypeVar('V')
WeightedPath = List[WeightedEdge]


if __name__ == "__main__":
    graph_Konigsberg: WeightedGraph[str] = WeightedGraph(["A", "B", "C", "D",
                                                          "a", "b", "c", "d", "e", "f", "g"])

    graph_Konigsberg.add_edge_by_vertices("A", "a", 1)
    graph_Konigsberg.add_edge_by_vertices("A", "b", 2)
    graph_Konigsberg.add_edge_by_vertices("A", "c", 3)
    graph_Konigsberg.add_edge_by_vertices("A", "d", 4)
    graph_Konigsberg.add_edge_by_vertices("A", "e", 5)
    
    graph_Konigsberg.add_edge_by_vertices("B", "a", 1)
    graph_Konigsberg.add_edge_by_vertices("B", "b", 2)
    graph_Konigsberg.add_edge_by_vertices("B", "f", 6)
    
    graph_Konigsberg.add_edge_by_vertices("C", "c", 3)
    graph_Konigsberg.add_edge_by_vertices("C", "d", 4)
    graph_Konigsberg.add_edge_by_vertices("C", "g", 7)
    
    graph_Konigsberg.add_edge_by_vertices("D", "e", 5)
    graph_Konigsberg.add_edge_by_vertices("D", "f", 6)
    graph_Konigsberg.add_edge_by_vertices("D", "g", 7)
    
    result: Optional[WeightedPath] = mst(graph_Konigsberg, 0)
    if result is None:
        print("No solution found!")
    else:
        print_weighted_path(graph_Konigsberg, result)
