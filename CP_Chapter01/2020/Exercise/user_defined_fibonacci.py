# Exercise 1.7 - 1
# title   : Fibonacci Sequence
# version : 1.0 (2020.08.03)
# author  : kobong

from typing import Dict, Tuple
from functools import lru_cache
from typing import Generator
import timeit


# function time_checker
def time_checker(func, n: int) -> Tuple[int, float]:
    start_time = timeit.default_timer()
    ret = func(n)
    elapsed_time = timeit.default_timer() - start_time
    return ret, elapsed_time
# end of time_checker (function)


# class CountChecker (decorator)
class CountChecker:
    def __init__(self, func):
        self.func = func
        self.cnt = 0

    def __call__(self, n: int):
        self.cnt += 1
        return self.func(n)

    def __del__(self):
        print("Call count for {}     : {} times".format(self.func.__name__, self.cnt))
# end of CountChecker (class)


# (2) Simple Fibonacci
@CountChecker
def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)


# (3) Memoization
# from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}


@CountChecker
def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


# (4) Memoization decorator
# from functools import lru_cache
@CountChecker
@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)


# (5) Simple for loop
@CountChecker
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
@CountChecker
def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    v_last: int = 0
    v_next: int = 1
    for _ in range(1, n):
        v_last, v_next = v_next, v_last + v_next
        yield v_next


# (7) User defined function
# lru_cache 사용 전에는 20까지만 연산하는게 제일 빠름
# lru_cache를 붙여 주면 더 빨라짐. ret의 값을 저장하고 있어서?
# 연산이 num = 100을 넘어가면 5보다는 느려짐.
# 저장 때문에 어쩔수 없는 듯.
# 대신 값을 저장한다는 장점이 있음 fib5 & fib6의 중간 정도?
@CountChecker
@lru_cache(maxsize=None)
def fib7(n: int) -> int:
    if n < 2:
        return 1

    ret = [0 for _ in range(n)]
    ret[0] = 1
    ret[1] = 1

    for idx in range(2, n):
        ret[idx] = ret[idx - 2] + ret[idx - 1]

    return ret[n - 1]
# end of fib7 (function)


if __name__ == "__main__":
    # fib2(5)  -> 15
    # fib2(10) -> 177
    # fib2(20) -> 21,891
    num: int = 2
    case: int = 6

    print("***** Fibonacci : {} *****". format(num))
    print("Simple Fibonacci        : fib2")
    print("Memoization             : fib3")
    print("Memoization decorator   : fib4")
    print("Simple for loop         : fib5 ")
    print("Generator and Fibonacci : fib6")
    print("User defined function   : fib7")
    print()

    v = [0 for _ in range(case)]
    et = [0.0 for _ in range(case)]

    v[0], et[0] = time_checker(fib2, num)
    # v[0], et[0] = 0, 0
    v[1], et[1] = time_checker(fib3, num)
    v[2], et[2] = time_checker(fib4, num)
    v[3], et[3] = time_checker(fib5, num)
    v[4], et[4] = time_checker(fib6, num)
    v[5], et[5] = time_checker(fib7, num)

    for i in range(case):
        print("Value for fib{}          : {}".format(i + 2, v[i]))
    print()

    for j in range(case):
        print("Elapsed time for fib{}   : {}".format(j + 2, et[j]))
    print()
