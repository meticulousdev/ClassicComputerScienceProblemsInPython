from __future__ import annotations
from typing import List
from data_point import DataPoint
from kmeans import KMeans


class Album(DataPoint):
    def __init__(self, name: str, year: int, length: float, tracks: float) -> None:
        super().__init__([length, tracks])
        self.name = name
        self.year = year
        self.length = length
        self.tracks = tracks

    def __repr__(self) -> str:
        return f"{self.name}, {self.year}"


if __name__ == "__main__":
    albums: List[Album] = [Album("Got to Be There", 1972, 35.45, 10), Album("Ben", 1972, 31.31, 10),
                           Album("Music & Me", 1973, 32.09, 10), Album("Forever, Michael", 1975, 33.36, 10),
                           Album("Off the Wall", 1979, 42.28, 10), Album("Thriller", 1982, 42.19, 9),
                           Album("Bad", 1987, 48.16, 10), Album("Dangerous", 1991, 77.03, 14),
                           Album("HIStory: Past, Present and Future, Book I", 1995, 148.58, 30),
                           Album("Invincible", 2001, 77.05, 16)]

    kmeans: KMeans[Album] = KMeans(2, albums)
    clusters: List[KMeans.Cluster] = kmeans.run()
    for index, cluster in enumerate(clusters):
        print(f"Cluster {index} Avg Length {cluster.centroid.dimensions[0]} "
              f"Avg Tracks {cluster.centroid.dimensions[1]}: {cluster.points}\n")
