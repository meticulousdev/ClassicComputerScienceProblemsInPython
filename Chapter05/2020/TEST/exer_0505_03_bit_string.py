from __future__ import annotations
from typing import Tuple, List
from CP_Chapter05.Example.chromosome import Chromosome
from CP_Chapter05.Example.genetic_algorithm import GeneticAlgorithm
from random import randrange, random
from copy import deepcopy
from secrets import token_bytes


class BitString(Chromosome):
    def __init__(self, x: bytes, y: bytes):
        self.x: bytes = x
        self.y: bytes = y

    def fitness(self) -> float:
        return 6 * self.x[0] - self.x[0] * self.x[0] + 4 * self.y[0] - self.y[0] * self.y[0]

    @classmethod
    def random_instance(cls) -> BitString:
        tb_x: bytes = token_bytes(1)
        tb_y: bytes = token_bytes(1)
        return BitString(tb_x, tb_y)

    def crossover(self, other: BitString) -> Tuple[BitString, BitString]:
        child1: BitString = deepcopy(self)
        child2: BitString = deepcopy(other)
        child1.y = other.y
        child2.y = self.y
        return child1, child2

    def mutate(self) -> None:
        if random() > 0.5:
            if random() > 0.5:
                self.x = (self.x[0] + 1).to_bytes(1, 'big')
            else:
                self.x = (self.x[0] - 1).to_bytes(1, 'big')
        else:
            if random() > 0.5:
                self.y = (self.y[0] + 1).to_bytes(1, 'big')
            else:
                self.y = (self.y[0] - 1).to_bytes(1, 'big')

    def __str__(self) -> str:
        return f"X: {self.x[0]} Y: {self.y[0]} 적합도: {self.fitness()}"


if __name__ == "__main__":
    initial_population: List[BitString] = [BitString.random_instance() for _ in range(20)]
    ga: GeneticAlgorithm[BitString] = GeneticAlgorithm(initial_population=initial_population,
                                                       threshold=13.0, max_generations=100,
                                                       mutation_chance=0.1, crossover_chance=0.7)
    result: BitString = ga.run()
    print(result)