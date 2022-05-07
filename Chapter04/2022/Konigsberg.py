from typing import TypeVar, List, Optional
from named_graph import NamedGraph
from named_edge import NamedEdge

from generic_search import Queue

from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge


V = TypeVar('V')
NamedPath = List[NamedEdge]


def eulerian_trail(ne: NamedEdge[V], start: int = 0) -> Optional[NamedPath]:
    if start > (ne.vertex_count - 1) or start < 0:
        return None
    
    result: NamedPath = []
    qe: Queue[NamedEdge] = Queue() 
    visited: List[bool] = [False] * ne.vertex_count

    def visit(index: int):
        visited[index] = True
        for edge in ne.edges_for_index(index):
            if not visited[edge.v]:
                ne.push(edge)

    visit(start)