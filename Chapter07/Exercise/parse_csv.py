# Exercise 7.9 - 2
import csv
from typing import List, Any
from CP_Chapter07.Example.util import normalize_by_feature_scaling
from CP_Chapter07.Example.network import Network
from random import shuffle


def parse_CSV(file_name: str,
              layer_structure: List[int], learning_rate: float,
              input_range: List[int], output_list: List[Any],
              train_range: List[int], test_range: List[int],
              species_pos: int = 0, max_iter: int = 10):

    data_parameters: List[List[float]] = []
    data_classifications: List[List[float]] = []
    data_species: List[Any] = []

    with open(file_name, mode='r') as data_file:
        data_set: List = list(csv.reader(data_file))
        shuffle(data_set)

        for data in data_set:
            parameters: List[float] = [float(n) for n in data[input_range[0]:input_range[1]]]
            data_parameters.append(parameters)
            species: Any = data[species_pos]

            if species == output_list[0]:
                data_classifications.append([1.0, 0.0, 0.0])
            elif species == output_list[1]:
                data_classifications.append([0.0, 1.0, 0.0])
            else:
                data_classifications.append([0.0, 0.0, 1.0])
            data_species.append(species)

    normalize_by_feature_scaling(data_parameters)

    # Network(layer_structure: List[int], learning_rate: float)
    data_network: Network = Network(layer_structure, learning_rate)

    def data_interpret_output(output: List[float]) -> Any:
        if max(output) == output[0]:
            return output_list[0]
        elif max(output) == output[1]:
            return output_list[1]
        else:
            return output_list[2]

    data_trainers: List[List[float]] = data_parameters[train_range[0]:train_range[1]]
    data_trainers_corrects: List[List[float]] = data_classifications[train_range[0]:train_range[1]]
    for _ in range(max_iter):
        data_network.train(data_trainers, data_trainers_corrects)

    data_testers: List[List[float]] = data_parameters[test_range[0]:test_range[1]]
    data_testers_corrects: List[str] = data_species[test_range[0]:test_range[1]]
    data_results = data_network.validate(data_testers, data_testers_corrects, data_interpret_output)
    print(f"정확도: {data_results[0]}/{data_results[1]} = {data_results[2] * 100}")


if __name__ == "__main__":
    print("iris classification")
    file_name: str = 'iris.csv'
    layer_structure: List[int] = [4, 6, 3]
    learning_rate: float = 0.3
    input_range = [0, 4]
    output_list: List[str] = ["Iris-setoa", "Iris-versicolor", "Iris-virginica"]
    train_range: List[int] = [0, 140]
    test_range: List[int] = [140, 150]
    species_pos: int = 4
    max_iter: int = 50
    parse_CSV(file_name, layer_structure, learning_rate, input_range, output_list,
              train_range, test_range, species_pos, max_iter)
    print()

    print("wine classification")
    file_name: str = 'wine.csv'
    layer_structure: List[int] = [13, 7, 3]
    learning_rate: float = 0.3
    input_range = [1, 14]
    output_list: List[str] = ['1', '2', '3']
    train_range: List[int] = [0, 150]
    test_range: List[int] = [150, 178]
    species_pos: int = 0
    max_iter: int = 10
    parse_CSV(file_name, layer_structure, learning_rate, input_range, output_list,
              train_range, test_range, species_pos, max_iter)
    print()
