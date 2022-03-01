# Exercise 7.9 - 1
import csv
from typing import List
from CP_Chapter07.Example.util import normalize_by_feature_scaling
from CP_Chapter07.Example.network import Network
from random import shuffle

if __name__ == "__main__":
    patient_parameters: List[List[float]] = []
    patient_classifications: List[List[float]] = []
    patient_status: List[int] = []

    # Import data from iris.csv file
    with open('parkinsons.csv', mode='r') as patient_file:
        patients: List = list(csv.reader(patient_file))
        shuffle(patients)

        for patient in patients:
            parameters: List[float] = [float(n) for n in patient[0:21]]
            patient_parameters.append(parameters)
            status: int = int(patient[22])

            if status == 1:
                patient_classifications.append([1.0, 0.0])
            else:
                patient_classifications.append([0.0, 1.0])
            patient_status.append(status)

    normalize_by_feature_scaling(patient_parameters)

    # Network(layer_structure: List[int], learning_rate: float)
    patient_network: Network = Network([21, 13, 2], 0.3)

    def patient_interpret_output(output: List[float]) -> int:
        if max(output) == output[0]:
            return 1
        else:
            return 0

    patient_trainers: List[List[float]] = patient_parameters[0:150]
    patient_trainers_corrects: List[List[float]] = patient_classifications[0:150]
    for _ in range(10):
        patient_network.train(patient_trainers, patient_trainers_corrects)

    patient_testers: List[List[float]] = patient_parameters[150:195]
    patient_testers_corrects: List[int] = patient_status[150:195]
    patient_results = patient_network.validate(patient_testers,
                                               patient_testers_corrects, patient_interpret_output)
    print(f"정확도: {patient_results[0]}/{patient_results[1]} = {patient_results[2] * 100}")
