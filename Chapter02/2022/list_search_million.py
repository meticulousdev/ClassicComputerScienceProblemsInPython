# Exercise 2.5 - 1
# title   : Performance of search algorithm
# version : 2022.03.02. 
# author  : kobong

import random
import timeit
from typing import List, Tuple, TypeVar
from generic_search import linear_contains, binary_contains

# Datatype modification
Codon = List[int]  # Codon Type Alias
Gene = List[Codon]  # Gene Type Alias


T = TypeVar('T')


def list_generation(list_len: int) -> List[T]:
    ret_list: List[T] = []
    for i in range(list_len):
        ret_list.append([i+1])

    return ret_list
# end of list_generation


def time_checker(func, int_list: List[int], num_target: List[int]) -> Tuple[bool, float]:
    start_time = timeit.default_timer()
    ret = func(int_list, num_target)
    elapsed_time = timeit.default_timer() - start_time
    return ret, elapsed_time
# end of time_checker


if __name__ == "__main__":
    # Random Number Generation
    num: int = 10**6
    num_list: List[int] = list_generation(num)

    num_test = [random.randint(1, num)]
    print("Search target                    : {}".format(num_test))

    v = [0 for _ in range(2)]
    et = [0.0 for _ in range(2)]

    v[0], et[0] = time_checker(linear_contains, num_list, num_test)
    print("Boolean for linear_contains      : {}".format(v[0]))
    print("Elapsed time for linear_contains : {}".format(et[0]))
    print()

    v[1], et[1] = time_checker(binary_contains, num_list, num_test)
    print("Boolean for binary_contains      : {}".format(v[1]))
    print("Elapsed time for binary_contains : {}".format(et[1]))
    print()
