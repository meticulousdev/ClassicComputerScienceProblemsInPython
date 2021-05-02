from typing import NamedTuple, List


class Item(NamedTuple):
    name: str
    weight: int
    value: float


def knapsack(items: List[Item], max_capacity: int) -> List[Item]:
    table: List[List[float]] = \
        [[0.0 for _ in range(max_capacity + 1)] for _ in range(len(items) + 1)]

    for i, item in enumerate(items):
        for capacity in range(1, max_capacity + 1):
            previous_items_value: float = table[i][capacity]
            if capacity >= item.weight:
                value_freeing_weight_for_item: float = table[i][capacity - item.weight]
                table[i + 1][capacity] = max(value_freeing_weight_for_item + item.value, previous_items_value)
            else:
                table[i + 1][capacity] = previous_items_value

    solution: List[Item] = []
    capacity = max_capacity
    for i in range(len(items), 0, -1):
        if table[i - 1][capacity] != table[i][capacity]:
            solution.append(items[i - 1])
            capacity -= items[i - 1].weight

    return solution


if __name__ == "__main__":
    items: List[Item] = [Item("TV", 50, 500),
                         Item("촛대", 2, 300),
                         Item("오디오", 35, 400),
                         Item("노트북", 3, 1000),
                         Item("식량", 15, 50),
                         Item("옷", 20, 800),
                         Item("보석", 1, 4000),
                         Item("책", 100, 300),
                         Item("프린터", 18, 30),
                         Item("냉장고", 200, 700),
                         Item("그림", 10, 1000)]

    # items: List[Item] = [Item("성냥", 1, 5),
    #                      Item("손전등", 2, 10),
    #                      Item("책", 1, 15)]

    print(knapsack(items, 75))
