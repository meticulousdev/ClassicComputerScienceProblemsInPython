from typing import TypeVar, Protocol, Iterable, List


T = TypeVar('T', bound="Comparable")


class Comparable(Protocol):
    def __eq__(self: T, other: T) -> bool:
        print("__eq__")
        return self == other

    def __lt__(self: T, other: T) -> bool:
        ...

    def __gt__(self: T, other: T) -> bool:
        ...

    def __le__(self: T, other: T) -> bool:
        ...

    def __ge__(self: T, other: T) -> bool:
        ...


if __name__ == "__main__":
    test01: T = 1
    test02: T = 2
    print(test01 == test02)

    test: List[T] = [1, 1]
    print(test[0] == test[1])
