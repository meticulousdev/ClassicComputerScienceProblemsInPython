from __future__ import annotations
from dataclasses import dataclass


# undirected graph
@dataclass
class Edge:
    u: int  # from vertex u
    v: int  # to vertex v

    def reversed(self) -> Edge:
        return Edge(self.v, self.u)

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}"
