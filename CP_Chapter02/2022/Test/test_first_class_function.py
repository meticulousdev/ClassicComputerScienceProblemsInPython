from typing import Callable


def add(a: int, b: int) -> int:
    print("add function")
    c = a + b
    print(f"{a} + {b} = {c}")
    return a + b


def print_func_name(func: Callable):
    print(func.__name__)


def run_func(func: Callable, *args) -> bool:
    func(args[0], args[1])


if __name__ == "__main__":
    print_func_name(add)
    run_func(add, 1, 2)
    # print_func_name(add(1, 2))  # error 