from typing import List, Callable
from math import exp


def dot_product(xs: List[float], ys: List[float]) -> float:
    return sum(x * y for x, y in zip(xs, ys))


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))


def derivative_sigmoid(x: float) -> float:
    sig: float = sigmoid(x)
    return sig * (1 - sig)


def tanh(x: float) -> float:
    return (1.0 - exp(-2.0 * x)) / (1.0 + exp(-2.0 * x))


def derivative_tanh(x: float) -> float:
    return (4.0 * exp(2.0 * x)) / (1.0 + exp(2.0 * x)) ** 2.0


def relu(x: float) -> float:
    return max(0.0, x)


def derivative_relu(x: float) -> float:
    return 1.0 if x > 0.0 else 0.0


def normalize_by_feature_scaling(dataset: List[List[float]]) -> None:
    for col_num in range(len(dataset[0])):
        column: List[float] = [row[col_num] for row in dataset]
        maximum = max(column)
        minimum = min(column)
        for row_num in range(len(dataset)):
            dataset[row_num][col_num] = (dataset[row_num][col_num] - minimum) / (maximum - minimum)
