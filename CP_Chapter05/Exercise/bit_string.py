# Exercise 5.8 - 3
from __future__ import annotations
from typing import Tuple, List
from CP_Chapter05.Example.chromosome import Chromosome
from CP_Chapter05.Example.genetic_algorithm import GeneticAlgorithm
from random import randrange, random
from copy import deepcopy
from secrets import token_bytes


class BitString(Chromosome):
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def fitness(self) -> float:
        return 6 * self.x - self.x * self.x + 4 * self.y - self.y * self.y

    def _bit_sub(self, bit_x: int, bit_y: int) -> int:
        len = bit_x.bit_length()
        sub = bit_x + (~bit_y) + 1
        return sub

    @classmethod
    def random_instance(cls) -> BitString:
        return BitString(randrange(100), randrange(100))

    def crossover(self, other: BitString) -> Tuple[BitString, BitString]:
        child1: BitString = deepcopy(self)
        child2: BitString = deepcopy(other)
        child1.y = other.y
        child2.y = self.y
        return child1, child2

    def mutate(self) -> None:
        if random() > 0.5:
            if random() > 0.5:
                self.x += 1
            else:
                self.x -= 1
        else:
            if random() > 0.5:
                self.y += 1
            else:
                self.y -= 1

    def __str__(self) -> str:
        return f"X: {self.x} Y: {self.y} 적합도: {self.fitness()}"


if __name__ == "__main__":
    # initial_population: List[BitString] = [BitString.random_instance() for _ in range(20)]
    # ga: GeneticAlgorithm[BitString] = GeneticAlgorithm(initial_population=initial_population,
    #                                                    threshold=13.0, max_generations=100,
    #                                                    mutation_chance=0.1, crossover_chance=0.7)
    # result: BitString = ga.run()
    # print(result)
    bit_x = 4
    bit_y = 2

    len = bit_x.bit_length()
    sub = bit_x + (~bit_y) + 1

    print(sub * 6)