from typing import TypeVar, Generic, List
T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

    def __len__(self) -> int:
        return len(self._container)


def hanoi_3towers(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int):
    num_moves = 0
    if n==1:
        end.push(begin.pop())
        return 1
    else:
        num_moves += hanoi_3towers(begin, temp, end, n-1)
        num_moves += hanoi_3towers(begin, end, temp, 1)
        num_moves += hanoi_3towers(temp, end, begin, n-1)
    return num_moves


def get_empty_towers(towers) -> List:
    return [i for i, n in enumerate(list(map(len, towers))) if n==0]


def hanoi_move_simple(towers, source, target) -> None:
    '''
    move discs by the amount of empty towers
    '''
    num_moves = 0
    # list of empty towers
    empty_towers = get_empty_towers(towers)
    # if target is empty: move target to empty_towers[0]
    # else: add target to empty_towers[0]
    if target in empty_towers: empty_towers.remove(target)
    empty_towers = [target] + empty_towers

    for i in empty_towers[::-1]:
        towers[i].push(towers[source].pop())
        num_moves += 1

    for i in empty_towers[1::]:
        towers[empty_towers[0]].push(towers[i].pop())
        num_moves += 1

    return num_moves

def hanoi_mtowers(towers):
    if len(towers)==3:
        return hanoi_3towers(towers[0], towers[2], towers[1], len(towers[0]))
    n_towers, n_discs = len(towers), len(towers[0])
    num_moves = 0
    # split until two empty towers left
    while len(towers[0])>len(get_empty_towers(towers))>2:
        # find first empty tower
        target_empty_tower = get_empty_towers(towers)[0]
        # move discs as many as possible
        num_moves += hanoi_move_simple(towers, source=0, target=target_empty_tower)
    num_moves += hanoi_3towers(towers[0], towers[-1], towers[-2], len(towers[0]))
    try:
        while len(towers[target_empty_tower])>0:
            num_moves += hanoi_move_simple(towers, source=target_empty_tower, target=len(towers)-1)
            target_empty_tower -= 1
        return num_moves
    except:
        return num_moves


n_discs: int = 8
n_towers: int = 9
towers = []
for _ in range(n_towers):
    towers.append(Stack())
for i in range(n_discs, 0, -1):
    towers[0].push(i)

total_moves = hanoi_mtowers(towers)

print(towers)
print(total_moves)