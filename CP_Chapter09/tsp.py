from typing import Dict, List, Iterable, Tuple
from itertools import permutations

vt_distances: Dict[str, Dict[str, int]] = {
    "Rutland":
        {"Burlington": 67,
         "White River Junction": 46,
         "Bennington": 55,
         "Brattleboro": 75},

    "Burlington":
        {"Rutland": 67,
         "White River Junction": 91,
         "Bennington": 122,
         "Brattleboro": 153},

    "White River Junction":
        {"Rutland": 46,
         "Burlington": 91,
         "Bennington": 98,
         "Brattleboro": 65},

    "Bennington":
        {"Rutland": 55,
         "Burlington": 122,
         "White River Junction": 98,
         "Brattleboro": 40},

    "Brattleboro":
        {"Rutland": 75,
         "Burlington": 153,
         "White River Junction": 65,
         "Bennington": 40}
}

vt_cities: Iterable[str] = vt_distances.keys()
city_permutations: Iterable[Tuple[str, ...]] = permutations(vt_cities)

tsp_paths: List[Tuple[str, ...]] = [c + (c[0],) for c in city_permutations]

if __name__ == "__main__":
    best_path: Tuple[str, ...]
    min_distance: int = 99999999999

    # print(len(tsp_paths))

    for path in tsp_paths:
        distance: int = 0
        last: str = path[0]

        for next in path[1:]:
            distance += vt_distances[last][next]
            last = next

        if distance < min_distance:
            min_distance = distance
            best_path = path

    print(f"최단 경로는 {best_path} 이고, {min_distance} 마일입니다.")
