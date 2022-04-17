from platform import node
from typing import TypeVar, List, Optional
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue

from dataclasses import dataclass
import matplotlib.pyplot as plt
import copy


plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.weight'] = 'bold'
plt.rcParams.update({'mathtext.default': 'default'})
plt.rcParams.update({'font.size': 11})


V = TypeVar('V')
WeightedPath = List[WeightedEdge]


# NamedTuple X
@dataclass
class XYPos:
    x: int
    y: int


def visualize_tree(wg: WeightedGraph, pq: PriorityQueue):
    depth = 4
    num_list = [i for i in range(0, depth) for j in range(0, 2 ** i)]
    num_list.insert(0, 0)
    xy: List[XYPos] = [XYPos(0, 0) for _ in range(0, (2 ** depth))]
    xy[1].x = 128
    xy[1].y = 2 ** depth
    for i in range(1, depth * 2):
        value_x = int(32 / (2 ** (num_list[i] - 1)))
        value_y = 2 ** (depth - 2)
        # left
        if (i * 2) < len(xy):
            xy[i * 2].x = xy[i].x - value_x
            xy[i * 2].y = xy[i].y - value_y

        # right
        if (i * 2 + 1) < len(xy):
            xy[i * 2 + 1].x = xy[i].x + value_x 
            xy[i * 2 + 1].y = xy[i].y - value_y

    edges: List[XYPos] = [XYPos(0, 0)]
    cnt = 1
    while not pq.empty:
        edge = pq.pop()
        x = xy[cnt].x
        y = xy[cnt].y
        plt.text(x, y, f"{wg.vertex_at(edge.u)} \n  ↓{edge.weight}\n{wg.vertex_at(edge.v)}")
        edges.append(xy[cnt])
        cnt += 1

    for i in range(1, len(edges)): 
        # left
        if (i * 2) < len(edges):
            plt.plot([edges[i].x, edges[i * 2].x], [edges[i].y, edges[i * 2].y], 'b')
        # right
        if (i * 2 + 1) < len(edges):   
            plt.plot([edges[i].x, edges[i * 2 + 1].x], [edges[i].y, edges[i * 2 + 1].y], 'b')

    plt.title("Minimum Spanning Tree\n(Priority Queue)")
    plt.xlim([0, xy[1].x * 2])
    plt.ylim([0, xy[1].y + value_y])
    plt.axis('off')
    plt.show()

def total_weight(wp: WeightedPath) -> float:
    return sum([e.weight for e in wp])

    
# def visit(index: int, visited: List[bool], wg: WeightedGraph, pq: PriorityQueue) -> None:
#     visited[index] = True
#     for edge in wg.edges_for_index(index):
#         if not visited[edge.v]:
#             pq.push(edge)


# def mst(wg: WeightedGraph[V], start: int = 0) -> Optional[WeightedPath]:
#     if start > (wg.vertex_count - 1) or start < 0:
#         return None

#     result: WeightedPath = []
#     pq: PriorityQueue[WeightedEdge] = PriorityQueue()
#     visited: List[bool] = [False] * wg.vertex_count

#     visit(start, visited, wg, pq)

#     while not pq.empty:
#         edge = pq.pop()
#         if visited[edge.v]:
#             continue

#         result.append(edge)
#         visit(edge.v, visited, wg, pq)

#     return result


# Jarnik's algorithm
# 1. Pick an arbitrary vertex to include tin the minimum spanning tree.
# 2. Find the lowest-weight edge connecting the minimum spanning tree 
#    to the vertices not yet in the minimum spanning tree.
# 3. Add the vertex at the end of that minimum edge to the minimum spanning tree.
# 4. Repeat steps 2 and 3 until every vertex in the graph is in the minimum spanning tree.

# mst : minimum spanning tree
def mst(wg: WeightedGraph[V], start: int = 0) -> Optional[WeightedPath]:
    if start > (wg.vertex_count - 1) or start < 0:
        return None

    result: WeightedPath = []
    pq: PriorityQueue[WeightedEdge] = PriorityQueue()
    visited: List[bool] = [False] * wg.vertex_count

    def visit(index: int):
        visited[index] = True
        for edge in wg.edges_for_index(index):
            if not visited[edge.v]:
                pq.push(edge)

    visit(start)
    # print(id(pq))
    visualize_tree(wg, copy.deepcopy(pq))

    while not pq.empty:
        edge = pq.pop()
        if visited[edge.v]:
            continue

        result.append(edge)
        visit(edge.v)
        visualize_tree(wg, copy.deepcopy(pq))
    return result


def print_weighted_path(wg: WeightedGraph, wp: WeightedPath) -> None:
    for edge in wp:
        print(f"{wg.vertex_at(edge.u)} {edge.weight}> {wg.vertex_at(edge.v)}")
    print(f"Total Weight: {total_weight(wp)}")


if __name__ == "__main__":
    # test basic Graph construction
    city_graph2: WeightedGraph[str] = WeightedGraph(["Seattle", "San Francisco", "Los Angeles", "Riverside",
                                                     "Phoenix", "Chicago", "Boston", "New York", "Atlanta", "Miami",
                                                     "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])

    city_graph2.add_edge_by_vertices("Seattle", "Chicago", 1737)
    city_graph2.add_edge_by_vertices("Seattle", "San Francisco", 678)
    city_graph2.add_edge_by_vertices("San Francisco", "Riverside", 386)
    city_graph2.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
    city_graph2.add_edge_by_vertices("Los Angeles", "Riverside", 50)
    city_graph2.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
    city_graph2.add_edge_by_vertices("Riverside", "Phoenix", 307)
    city_graph2.add_edge_by_vertices("Riverside", "Chicago", 1704)
    city_graph2.add_edge_by_vertices("Phoenix", "Dallas", 887)
    city_graph2.add_edge_by_vertices("Phoenix", "Houston", 1015)
    city_graph2.add_edge_by_vertices("Dallas", "Chicago", 805)
    city_graph2.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph2.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph2.add_edge_by_vertices("Houston", "Atlanta", 702)
    city_graph2.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph2.add_edge_by_vertices("Atlanta", "Chicago", 588)
    city_graph2.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph2.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph2.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph2.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph2.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph2.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph2.add_edge_by_vertices("Detroit", "New York", 482)
    city_graph2.add_edge_by_vertices("Boston", "New York", 190)
    city_graph2.add_edge_by_vertices("New York", "Philadelphia", 81)
    city_graph2.add_edge_by_vertices("Philadelphia", "Washington", 123)

    result: Optional[WeightedPath] = mst(city_graph2, 0)
    if result is None:
        print("No solution found!")
    else:
        print_weighted_path(city_graph2, result)
