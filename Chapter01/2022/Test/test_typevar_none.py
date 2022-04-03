from typing import TypeVar


T = TypeVar('T', int, None) 


def add(a: T, b: T) -> T:
    return a + b


if __name__ == "__main__":
    print(add("AAA", "BBB"))
