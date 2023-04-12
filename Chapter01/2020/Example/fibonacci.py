# %%
from typing import Dict
from functools import lru_cache
from typing import Generator
import time


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
    num: int = 40

    print(f"***** Fibonacci              : {num} *****\n")
    
    print("Simple Fibonacci             : ", end="")
    time_start = time.time()
    print(fib2(num))
    time_end = time.time()
    print(f"Simple Fibonacci took        : {time_end - time_start}s\n")

    print("Memoization                  : ", end="")
    time_start = time.time()
    print(fib3(num))
    time_end = time.time()
    print(f"Memoization took             : {time_end - time_start}s\n")    

    print("Memoization decorator        : ", end="")
    time_start = time.time()
    print(fib4(num))
    time_end = time.time()
    print(f"Memoization took             : {time_end - time_start}s\n")    

    print("Simple for loop              : ", end="")
    time_start = time.time()
    print(fib5(num))
    time_end = time.time()
    print(f"Simple for loop took         : {time_end - time_start}s\n")    

    print("Generator and Fibonacci      : ", end="")
    time_start = time.time()
    print(fib6(num))
    time_end = time.time()
    print(f"Generator and Fibonacci took : {time_end - time_start}s\n")
