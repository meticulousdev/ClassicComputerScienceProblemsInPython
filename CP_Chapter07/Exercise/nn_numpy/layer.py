from __future__ import annotations
from typing import List, Callable, Optional

import numpy

from CP_Chapter07.Exercise.nn_numpy.neuron import Neuron
from CP_Chapter07.Exercise.nn_numpy.util import dot_product, sigmoid, derivative_sigmoid


class Layer:
    def __init__(self, previous_layer: Optional[Layer], num_neurons: int,
                 learning_rate: float, activation_function: Callable[[float], float],
                 derivative_activation_function: Callable[[float], float]) -> None:
        self.previous_layer: Optional[Layer] = previous_layer
        self.neurons: List[Neuron] = []

        for i in range(num_neurons):
            if previous_layer is None:
                # input layer
                random_weights: numpy.ndarray = numpy.array([])
            else:
                random_weights = numpy.random.rand(len(previous_layer.neurons))

            neuron: Neuron = Neuron(random_weights, learning_rate,
                                    activation_function, derivative_activation_function)
            self.neurons.append(neuron)

        self.output_cache: numpy.ndarray = numpy.zeros((1, num_neurons))

    def outputs(self, inputs: numpy.ndarray) -> numpy.ndarray:
        if self.previous_layer is None:
            self.output_cache = inputs
        else:
            self.output_cache = numpy.array([n.output(inputs) for n in self.neurons])
        return self.output_cache

    def calculate_deltas_for_output_layer(self, expected: numpy.ndarray) -> None:
        for n in range(len(self.neurons)):
            self.neurons[n].delta = self.neurons[n].derivative_activation_function(self.neurons[n].output_cache) * (expected[n] - self.output_cache[n])

    def calculate_deltas_for_hidden_layer(self, next_layer: Layer) -> None:
        for index, neuron in enumerate(self.neurons):
            next_weights: numpy.ndarray = numpy.array([n.weights[index] for n in next_layer.neurons])
            next_deltas: numpy.ndarray = numpy.array([n.delta for n in next_layer.neurons])
            sum_weights_and_deltas: float = dot_product(next_weights, next_deltas)
            neuron.delta = neuron.derivative_activation_function(neuron.output_cache) * sum_weights_and_deltas


# if __name__ == "__main__":
#     layer_structure = 3
#     learning_rate = 0.3
#     input_layer: Layer = Layer(None, layer_structure, learning_rate,
#                                sigmoid, derivative_sigmoid)
