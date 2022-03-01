import torch
from typing import List


def sigmoid(x: torch.float) -> torch.float:
    return 1.0 / (1.0 + torch.exp(-x))


def derivative_sigmoid(x: torch.float) -> torch.float:
    sig: torch.float = sigmoid(x)
    return sig * (1 - sig)


def normalize_by_feature_scaling(dataset: List[List[float]]) -> None:
    for col_num in range(len(dataset[0])):
        column: List[float] = [row[col_num] for row in dataset]
        maximum = max(column)
        minimum = min(column)
        for row_num in range(len(dataset)):
            dataset[row_num][col_num] = (dataset[row_num][col_num] - minimum) / (maximum - minimum)
