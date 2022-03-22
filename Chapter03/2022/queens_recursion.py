from typing import List


pos: List[int] = [0] * 8
flag_a: List[bool] = [False] * 8
flag_b: List[bool] = [False] * 15
flag_c: List[bool] = [False] * 15


def put_queens(pos: List[int]) -> None:
    for j in range(8):
        for i in range(8):
            print("■" if pos[i] == j else '□', end="")
        print()
    print()


def set_queens(queen: int) -> None:
    for j in range(8):
        if(not flag_a[j] and not flag_b[queen + j] and not flag_c[queen - j + 7]):
            pos[queen] = j
            if queen == 7:
                put_queens(pos)
                print()
            else:
                flag_a[j] = flag_b[queen + j] = flag_c[queen - j + 7] = True
                set_queens(queen + 1)
                flag_a[j] = flag_b[queen + j] = flag_c[queen - j + 7] = False
                

if __name__ == "__main__":
    set_queens(0)
