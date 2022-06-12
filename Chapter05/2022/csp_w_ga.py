import random
from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod
from genetic_algorithm import GeneticAlgorithm


V = TypeVar('V')
D = TypeVar('D')


# class Constraint(Generic[V, D], metaclass=ABCMeta):
# class Constraint(Generic[V, D]):
class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
            ...
            # pass
        

class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}

        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("모든 변수에 도메인이 할당되어야 합니다.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("제약 조건 변수가 아닙니다.")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True
    
    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        if len(assignment) == len(self.variables):
            return assignment
        
        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            # local_assignment = assignment
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None

    # Add a new function to the constraint-satisfaction framework from chapter 3
    # that solves any arbitrary CSP using a genetic algorithm. A possible measure of
    # fitness is the number of constraints that are resolved by a chromosome.

    def fitness(self):

    def crossover(self):

    def mutate(self):

    def __str__(self):

    def random_instance(self) -> Dict[V, D]:
        assignment: Dict[V, D] = {}
        for variable in self.variables:
            assignment[variable] = random.choice(self.domains[variable])
        return assignment

    def test_genetic_algorithm(self):
        print("test genetic algorithm")
        initial_population: List[Dict[V, D]] = [self.random_instance() for _ in range(100)]
        ga: GeneticAlgorithm[Dict[V, D]] = GeneticAlgorithm(initial_population=initial_population,
                                                            threshold=1.0, max_generations=100,
                                                            mutation_chance=0.2, crossover_chance=0.7,
                                                            selection_type=GeneticAlgorithm.SelectionType.TOURNAMENT)
        print()
