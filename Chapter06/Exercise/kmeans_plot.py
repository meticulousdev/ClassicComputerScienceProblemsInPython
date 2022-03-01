# Exercise 6.7 - 1 and 2
from __future__ import annotations
from typing import List
import csv
from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np

from CP_Chapter06.Example.data_point import DataPoint
from CP_Chapter06.Example.kmeans import KMeans


class Governor(DataPoint):
    def __init__(self, longitude: float, age: float, state: str) -> None:
        super().__init__([longitude, age])
        self.longitude = longitude
        self.age = age
        self.state = state

    def __repr__(self) -> str:
        return f"{self.state}: (경도: {self.longitude}, 나이: {self.age})"


@dataclass
class SCPoint:
    age: np.ndarray
    longitude: np.ndarray


if __name__ == "__main__":
    # Import data from *.csv file
    fp = open("governors.csv", "r", encoding="utf-8")
    governors_csv = csv.reader(fp)

    governors: List[Governor] = []
    for governor in governors_csv:
        gov_longitude: float = float(governor[0])
        gov_age: float = float(governor[1])
        gov_state: str = governor[2]
        governors.append(Governor(gov_longitude, gov_age, gov_state))

    # Run k-mean clustering
    num_cluster = 2
    kmeans: KMeans[Governor] = KMeans(num_cluster, governors)
    gov_clusters: List[KMeans.Cluster] = kmeans.run()

    for index, cluster in enumerate(gov_clusters):
        print(f"Cluster {index}: {cluster.points}\n")

    # Assignment
    scpoints: List[SCPoint] = []
    for i in range(num_cluster):
        idx_len = len(gov_clusters[i].points)
        age: np.ndarray = np.zeros([1, idx_len])
        longitude: np.ndarray = np.zeros([1, idx_len])
        scpoint: SCPoint = SCPoint(age, longitude)

        for j in range(idx_len):
            scpoint.age[0][j] = gov_clusters[i].points[j].age
            scpoint.longitude[0][j] = gov_clusters[i].points[j].longitude

        scpoints.append(scpoint)

    # Scatter plot
    plt.scatter(scpoints[0].longitude, scpoints[0].age, marker="o", c="black")
    plt.scatter(scpoints[1].longitude, scpoints[1].age, marker="s", c="blue")
    plt.xlabel("longitude")
    plt.ylabel("age")
    plt.show()

    fp.close()
