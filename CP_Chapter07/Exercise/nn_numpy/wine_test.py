import csv
from typing import List
from util import normalize_by_feature_scaling
from network import Network
from random import shuffle
import numpy

if __name__ == "__main__":
    wine_parameters: List[List[float]] = []
    wine_classifications: List[List[float]] = []
    wine_species: List[int] = []

    # Import data from wine.csv file
    with open('wine.csv', mode='r') as wine_file:
        wines: List = list(csv.reader(wine_file, quoting=csv.QUOTE_NONNUMERIC))
        shuffle(wines)

        for wine in wines:
            parameters: List[float] = [float(n) for n in wine[1:14]]
            wine_parameters.append(parameters)
            species: int = wine[0]

            if species == 1:
                wine_classifications.append([1.0, 0.0, 0.0])
            elif species == 2:
                wine_classifications.append([0.0, 1.0, 0.0])
            else:
                wine_classifications.append([0.0, 0.0, 1.0])
            wine_species.append(species)

    normalize_by_feature_scaling(wine_parameters)

    # Network(layer_structure: List[int], learning_rate: float)
    wine_network: Network = Network([13, 7, 3], 0.3)

    def wine_interpret_output(output: numpy.ndarray) -> int:
        if max(output) == output[0]:
            return 1
        elif max(output) == output[1]:
            return 2
        else:
            return 3

    wine_trainers: numpy.ndarray = numpy.array(wine_parameters[0:150])
    wine_trainers_corrects: numpy.ndarray = numpy.array(wine_classifications[0:150])
    for _ in range(10):
        wine_network.train(wine_trainers, wine_trainers_corrects)

    wine_testers: numpy.ndarray = numpy.array(wine_parameters[150:178])
    wine_testers_corrects: numpy.ndarray = numpy.array(wine_species[150:178])
    wine_results = wine_network.validate(wine_testers, wine_testers_corrects, wine_interpret_output)
    print(f"정확도: {wine_results[0]}/{wine_results[1]} = {wine_results[2] * 100}")
