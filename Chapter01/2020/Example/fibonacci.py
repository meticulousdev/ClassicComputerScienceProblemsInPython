# %%
from typing import Dict, Tuple
from functools import lru_cache
from typing import Generator


# %%
# (2) Simple Fibonacci
def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)


# (3) Memoization
# from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


# (4) Memoization decorator
# from functools import lru_cache
@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)


# (5) Simple for loop
def fib5(n: int) -> int:
    if n == 0:
        return n
    v_last: int = 0
    v_next: int = 1
    for _ in range(1, n):
        v_last, v_next = v_next, v_last + v_next
    return v_next


# (6) Generator and Fibonacci
# from typing import Generator
def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    v_last: int = 0
    v_next: int = 1
    for _ in range(1, n):
        v_last, v_next = v_next, v_last + v_next
        yield v_next


# %%
if __name__ == "__main__":
    # fib2(5)  -> 15
    # fib2(10) -> 177
    # fib2(20) -> 21,891
    num: int = 5

    print("***** Fibonacci : {} *****". format(num))
    print("Simple Fibonacci        : fib2")
    print("Memoization             : fib3")
    print("Memoization decorator   : fib4")
    print("Simple for loop         : fib5 ")
    print("Generator and Fibonacci : fib6")
    print()

    print(fib2(num))
    print(fib3(num))
    print(fib4(num))
    print(fib5(num))
    print(fib6(num))
