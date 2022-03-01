from typing import Generic, TypeVar, List, Iterator, Tuple
from random import choice
from dataclasses import dataclass
from functools import partial
from CP_Chapter06.Example.data_point import DataPoint


Point = TypeVar('Point', bound=DataPoint)


class KMeans(Generic[Point]):
    @dataclass
    class Cluster:
        points: List[Point]
        centroid: DataPoint

    def __init__(self, k: int, points: List[Point]) -> None:
        if k < 1:
            raise ValueError("k must be >= 1")

        self._points: List[Point] = points
        self._clusters: List[KMeans.Cluster] = []

        idx: int = self._points.index(choice(self._points))
        center: DataPoint = self._points.pop(idx)
        for _ in range(k - 1):
            center: DataPoint = self._choice_next(center)
            cluster: KMeans.Cluster = KMeans.Cluster([], center)
            self._clusters.append(cluster)

    def _choice_next(self, center: DataPoint) -> DataPoint:
        differences: List[float] = [DataPoint.distance(center, point) for point in self._points]
        probabilities: List[float] = [DataPoint.distance(center, point) / sum(differences) for point in self._points]
        idx: int = probabilities.index(max(probabilities))
        return self._points.pop(idx)


if __name__ == "__main__":
    point1: DataPoint = DataPoint([2.0, 1.0, 1.0])
    point2: DataPoint = DataPoint([2.0, 2.0, 5.0])
    point3: DataPoint = DataPoint([3.0, 1.5, 2.5])
    point4: DataPoint = DataPoint([1.0, 2.0, 3.5])
    kmeans_test: KMeans[DataPoint] = KMeans(2, [point1, point2, point3, point4])
