from __future__ import annotations
from dataclasses import dataclass
from edge import Edge


@dataclass
class NamedEdge(Edge):
    u_name: str
    v_name: str

    def reversed(self) -> NamedEdge:
        return NamedEdge(self.v, self.u, self.v_name, self.u_name)

    def __str__(self) -> str:
        return f"{self.u} {self.u_name} -> {self.v} {self.v_name}"
