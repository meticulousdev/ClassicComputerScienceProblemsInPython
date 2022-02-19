# Exercise 1.7 - 3
# title   : Infinite tower of Hanoi
# version : 2022.02.20.
# author  : kobong
from asyncio import protocols
from typing import TypeVar, Generic, List
from wsgiref.util import request_uri

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    # check disk size
    def check(self) -> bool:
        len_container = len(self._container)
        if len_container > 1:
            # for i in range(len_container):
            #     print(self._container[i], end="")
            # print()
            for i in range(len_container - 1):
                if self._container[i] > self._container[i+1]:
                    return False
        return True

    def __repr__(self) -> str:
        return repr(self._container)


# from : begin
# to : end
# by : by
def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
        # check each tower
        if begin.check() and temp.check() and end.check():
            pass
        else:
            raise ValueError
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)
# end of hanoi


# 정상적으로 동작하는지 확인하기 위해서 List type의 towers 반환
def multiple_hanoi(nt: int, nd: int) -> List:
    # nt : the number of towers
    # nd : the number of discs
    # Initialization
    towers: List = []
    for _ in range(nt):
        towers.append(Stack())

    for i in range(1, nd + 1):
        towers[0].push(i)

    # Distribution of Discs
    # 각 탑을 최소 1번 이상 거칠 수 있도록 탑에 들어갈 disc 수 결정
    nd_mv = [0 for _ in range(nt - 2)]
    cnt = 0
    while cnt < nd - 1:
        for j in range(nt - 2):
            nd_mv[j] += 1
            cnt += 1
            if cnt == nd - 1:
                break

    while 0 in nd_mv:
        nd_mv.remove(0)

    # Hanoi Tower : Recursion and for loop
    # 분배된 각 탑에서 최종 위치로 이동하기 위한 동작들
    # 1. 시작 탑(0)에서 마지막 탑(-1)을 제외한 모든 탑에 원반 분배
    # 2. 제일 큰 원반을 중간 탑(1)을 거쳐서 마지막 탑으로 이동
    # 3. 각각의 탑에 있던 원반을 빈 탑인 시작 탑(0)을 거쳐서 마지막 탑으로 이동
    temp = 1
    rep = len(nd_mv)

    for i in range(rep):
        hanoi(towers[0], towers[i + 1], towers[-1], nd_mv[i])

    # for i in range(nt):
    #     print(towers[i])
    # print()

    hanoi(towers[0], towers[-1], towers[temp], 1)

    # for i in range(nt):
    #     print(towers[i])
    # print()

    for i in range(rep):
        hanoi(towers[rep - i], towers[-1], towers[0], nd_mv[(rep - 1) - i])

    # for i in range(nt):
    #     print(towers[i])
    # print()

    return towers
# end of multiple_hanoi


def check_hanoi_result(towers: List, nt: int, nd: int) -> None:
    for i in range(nd):
        if (towers[nt - 1].pop()) != (nd - i):
            return "BAD!"
        else:
            return "GOOD!"
# end of check_hanoi_result


if __name__ == "__main__":
    for idx in range(3, 20):
        for jdx in range(3, 20):
            num_towers: int = idx
            num_discs: int = jdx
            ret_towers: List = multiple_hanoi(num_towers, num_discs)
            answer: str = check_hanoi_result(ret_towers, num_towers, num_discs)
            
            print(f"{num_towers} towers with {num_discs} discs: {answer}")
            
            assert answer == "GOOD!"
