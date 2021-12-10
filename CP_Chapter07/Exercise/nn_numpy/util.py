import numpy
from math import exp


def dot_product(xs: numpy.ndarray, ys: numpy.ndarray) -> float:
    return numpy.sum([x * y for x, y in zip(xs, ys)])


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + numpy.exp(-x))


def derivative_sigmoid(x: float) -> float:
    sig: float = sigmoid(x)
    return sig * (1 - sig)


def normalize_by_feature_scaling(dataset: numpy.ndarray) -> None:
    for col_num in range(len(dataset[0])):
        column: numpy.ndarray = numpy.array([row[col_num] for row in dataset])
        maximum = max(column)
        minimum = min(column)
        for row_num in range(len(dataset)):
            dataset[row_num][col_num] = (dataset[row_num][col_num] - minimum) / (maximum - minimum)

# if __name__ == "__main__":
#     xs: numpy.ndarray = numpy.array([1, 2, 3])
#     ys: numpy.ndarray = numpy.array([4, 5, 6])
#     print(dot_product(xs, ys))
#
#     two_darray: numpy.ndarray = numpy.array([[1.0, 2.0, 3.0],
#                                              [4.0, 5.0, 6.0],
#                                              [7.0, 8.0, 9.0]])
#     print(two_darray)
#     print(type(two_darray))
#
#     normalize_by_feature_scaling(two_darray)
#
#     print(two_darray)
#     print(type(two_darray))
