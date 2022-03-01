import torch
import torch.nn as nn
import numpy
from typing import Callable, Tuple, List
from CP_Chapter07.Exercise.nn_pytorch.util import sigmoid, derivative_sigmoid


class NeuralNetwork(nn.Module):
    def __init__(self, layer_structure: List[int], learning_rate: float):
        super(NeuralNetwork, self).__init__()
        if len(layer_structure) < 3:
            raise ValueError("오류: 최소 3개의 층이 필요합니다(입력층, 은닉층, 출력층)!")

        self.input_size: int = layer_structure[0]
        self.hidden_size: int = layer_structure[1]
        self.output_size: int = layer_structure[2]

        self.learning_rate: float = learning_rate

        self.z1 = 0
        self.h1 = 0
        self.z2 = 0

        self.weight_ih: torch.Tensor = torch.randn(self.input_size, self.hidden_size)
        self.weight_ho: torch.Tensor = torch.randn(self.hidden_size, self.output_size)

    def outputs(self, input, weights):
        return sigmoid(torch.matmul(input, weights))

    def update_weights(self, inputs, outputs, expecteds) -> None:
        o_error = outputs - expecteds
        o_delta = o_error * derivative_sigmoid(expecteds)

        h1_error = torch.matmul(o_delta, torch.t(self.weight_ho))
        h1_delta = h1_error * derivative_sigmoid(self.h1)

        self.weight_ih = self.weight_ih + self.learning_rate * torch.matmul(torch.t(inputs), h1_delta)
        self.weight_ho = self.weight_ho + self.learning_rate * torch.matmul(torch.t(self.h1), o_delta)

    def forward(self, X):
        self.z1 = torch.matmul(X, self.weight_ih)
        self.h1 = sigmoid(self.z1)
        self.z2 = torch.matmul(self.h1, self.weight_ho)
        o: torch.float = sigmoid(self.z2)
        return o

    def train_nn(self, inputs, outputs):
        expecteds = self.forward(inputs)
        self.update_weights(inputs, outputs, expecteds)

    def validate(self, inputs, expecteds, interpret_output) -> Tuple[int, int, float]:
        correct: int = 0
        for input, expected in zip(inputs, expecteds):
            result = interpret_output(self.forward(input))
            if result == expected:
                correct += 1

        percentage: float = correct / len(inputs)
        return correct, len(inputs), percentage
