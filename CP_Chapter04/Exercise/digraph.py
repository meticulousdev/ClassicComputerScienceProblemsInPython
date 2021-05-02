# Exercise 4.7 - 2
from typing import TypeVar, Generic, List, Optional
from CP_Chapter04.Example.edge import Edge

V = TypeVar('V')


class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))

    # 그래프에 정점을 추가하고 인덱스를 반환한다.
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    # 무향(undirected) 그래프이므로 항상 양방향으로 에지를 추가한다.
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    # 정점 인덱스를 사용하여 에지를 추가한다(헬퍼 메서드).
    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    # 정점 인덱스를 참조하여 에지를 추가한다(헬퍼 메서드).
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    # 특정 인덱스에서 정점을 찾는다.
    def vertex_at(self, index: int) -> int:
        return self._vertices[index]

    # 정점 인덱스를 찾는다.
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    # 정점 인덱스에 연결된 이웃 정점을 찾는다.
    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    # 정점의 이웃 정점을 찾는다(헬퍼 메서드).
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))

    # 정점 인덱스에 연결된 모든 에지를 반환한다.
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    # 정점의 해당 에지를 반환한다(헬퍼 메서드).
    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    # 유향(directed) 그래프이므로 단방향으로 에지를 추가한다.
    def digraph_add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)

    # 정점 인덱스를 사용하여 에지를 추가한다(헬퍼 메서드).
    def digraph_add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.digraph_add_edge(edge)

    # 정점 인덱스를 참조하여 에지를 추가한다(헬퍼 메서드).
    def digraph_add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.digraph_add_edge_by_indices(u, v)

    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc


if __name__ == "__main__":
    # test basic Graph construction
    city_graph: Graph[str] = Graph(["Seattle", "San Francisco", "Los Angeles", "Riverside",
                                    "Phoenix", "Chicago", "Boston", "New York", "Atlanta", "Miami",
                                    "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])

    city_graph.digraph_add_edge_by_vertices("Seattle", "Chicago")
    city_graph.digraph_add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.digraph_add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.digraph_add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.digraph_add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.digraph_add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.digraph_add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.digraph_add_edge_by_vertices("Riverside", "Chicago")
    city_graph.digraph_add_edge_by_vertices("Phoenix", "Dallas")
    city_graph.digraph_add_edge_by_vertices("Phoenix", "Houston")
    city_graph.digraph_add_edge_by_vertices("Dallas", "Chicago")
    city_graph.digraph_add_edge_by_vertices("Dallas", "Atlanta")
    city_graph.digraph_add_edge_by_vertices("Dallas", "Houston")
    city_graph.digraph_add_edge_by_vertices("Houston", "Atlanta")
    city_graph.digraph_add_edge_by_vertices("Houston", "Miami")
    city_graph.digraph_add_edge_by_vertices("Atlanta", "Chicago")
    city_graph.digraph_add_edge_by_vertices("Atlanta", "Washington")
    city_graph.digraph_add_edge_by_vertices("Atlanta", "Miami")
    city_graph.digraph_add_edge_by_vertices("Miami", "Washington")
    city_graph.digraph_add_edge_by_vertices("Chicago", "Detroit")
    city_graph.digraph_add_edge_by_vertices("Detroit", "Boston")
    city_graph.digraph_add_edge_by_vertices("Detroit", "Washington")
    city_graph.digraph_add_edge_by_vertices("Detroit", "New York")
    city_graph.digraph_add_edge_by_vertices("Boston", "New York")
    city_graph.digraph_add_edge_by_vertices("New York", "Philadelphia")
    city_graph.digraph_add_edge_by_vertices("Philadelphia", "Washington")
    print(city_graph)
