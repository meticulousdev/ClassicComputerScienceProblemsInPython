from typing import TypeVar, Generic


T = TypeVar('T', int, float) 


# class TestClass(Generic[T]):
#     def add(a: T, b: T) -> T:
#         return a + b


def add(a: T, b: T) -> T:
    return a + b


if __name__ == "__main__":
    print(add("AAA", "BBB"))
