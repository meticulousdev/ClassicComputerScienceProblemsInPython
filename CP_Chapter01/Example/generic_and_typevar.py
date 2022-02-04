from typing import TypeVar


T = TypeVar('N', int, float)


if __name__ == "__main__":
    print(f"T: {T.__name__}")