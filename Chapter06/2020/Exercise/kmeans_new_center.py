# Exercise 6.7 - 3
from __future__ import annotations
from typing import TypeVar, Generic, List, Sequence
from copy import deepcopy
from functools import partial
from random import uniform
from statistics import mean, pstdev
from dataclasses import dataclass
from CP_Chapter06.Example.data_point import DataPoint


def zscores(original: Sequence[float]) -> List[float]:
    avg: float = mean(original)
    std: float = pstdev(original)
    if std == 0:
        return [0] * len(original)
    return [(x - avg) / std for x in original]


Point = TypeVar('Point', bound=DataPoint)


class KMeans(Generic[Point]):
    @dataclass
    class Cluster:
        points: List[Point]
        centroid: DataPoint

    def __init__(self, k: int, points: List[Point], centers: List[Point]) -> None:
        if k < 1:
            raise ValueError("k must be >= 1")

        if k != len(centers):
            raise ValueError("The length of centers must be k")

        self._points: List[Point] = points
        self._zscore_normalize()
        self._clusters: List[KMeans.Cluster] = []
        for center in centers:
            cluster: KMeans.Cluster = KMeans.Cluster([], center)
            self._clusters.append(cluster)

    @property
    def _centroids(self) -> List[DataPoint]:
        return [x.centroid for x in self._clusters]

    def _dimension_slice(self, dimension: int) -> List[float]:
        return [x.dimensions[dimension] for x in self._points]

    def _zscore_normalize(self) -> None:
        zscored: List[List[float]] = [[] for _ in range(len(self._points))]
        for dimension in range(self._points[0].num_dimensions):
            dimension_slice: List[float] = self._dimension_slice(dimension)

            for index, zscore in enumerate(zscores(dimension_slice)):
                zscored[index].append(zscore)

        for i in range(len(self._points)):
            self._points[i].dimensions = tuple(zscored[i])

    def _assign_clusters(self) -> None:
        for point in self._points:
            closest: DataPoint = min(self._centroids, key=partial(DataPoint.distance, point))
            idx: int = self._centroids.index(closest)
            cluster: KMeans.Cluster = self._clusters[idx]
            cluster.points.append(point)

    def _generate_centroids(self) -> None:
        for cluster in self._clusters:
            if len(cluster.points) == 0:
                continue

            means: List[float] = []
            for dimension in range(cluster.points[0].num_dimensions):
                dimension_slice: List[float] = [p.dimensions[dimension] for p in cluster.points]
                means.append(mean(dimension_slice))

            cluster.centroid = DataPoint(means)

    def run(self, max_iterations: int = 100) -> List[KMeans.Cluster]:
        for iteration in range(max_iterations):
            for cluster in self._clusters:
                cluster.points.clear()

            self._assign_clusters()
            old_centroids: List[DataPoint] = deepcopy(self._centroids)
            self._generate_centroids()

            if old_centroids == self._centroids:
                print(f"{iteration}회 반복 후 수렴")
                return self._clusters

        return self._clusters


if __name__ == "__main__":
    point1: DataPoint = DataPoint([2.0, 1.0, 1.0])
    point2: DataPoint = DataPoint([2.0, 2.0, 5.0])
    point3: DataPoint = DataPoint([3.0, 1.5, 2.5])

    center1: DataPoint = DataPoint([1, 1, 1])
    center2: DataPoint = DataPoint([1, 1, 1])

    kmeans_test: KMeans[DataPoint] = KMeans(2, [point1, point2, point3], [center1, center2])
    test_cluster: List[KMeans.Cluster] = kmeans_test.run()
    for index, cluster in enumerate(test_cluster):
        print(f"군집 {index}: {cluster.points}")
