from typing import List

if __name__ == "__main__":
    a: List[int] = [1, 2, 3]
    b = a

    print(a)
    print(id(a))
    print()

    print(b)
    print(id(b))
    print()

    b.append(4)

    print(a)
    print(id(a))
    print()

    print(b)
    print(id(b))
    print()
