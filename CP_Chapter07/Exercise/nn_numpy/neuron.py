import numpy
from typing import Callable
from CP_Chapter07.Exercise.nn_numpy.util import dot_product, sigmoid, derivative_sigmoid


class Neuron:
    def __init__(self, weights: numpy.ndarray, learning_rate: float,
                 activation_function: Callable[[float], float],
                 derivative_activation_function: Callable[[float], float]) -> None:
        self.weights: numpy.ndarray = weights
        self.activation_function: Callable[[float], float] = activation_function
        self.derivative_activation_function: Callable[[float], float] = derivative_activation_function
        self.learning_rate: float = learning_rate
        self.output_cache: float = 0.0
        self.delta: float = 0.0

    def output(self, inputs: numpy.ndarray) -> float:
        self.output_cache = dot_product(inputs, self.weights)
        return self.activation_function(self.output_cache)

# if __name__ == "__main__":
#     weights: numpy.ndarray = numpy.array([1, 2, 3, 4, 5, 6])
#     learning_rate: float = 0.3
#     neuron: Neuron = Neuron(weights, learning_rate, sigmoid, derivative_sigmoid)
#
#     inputs: numpy.ndarray = numpy.array([2, 3, 4, 5, 6, 7])
#     print(neuron.output(inputs))
