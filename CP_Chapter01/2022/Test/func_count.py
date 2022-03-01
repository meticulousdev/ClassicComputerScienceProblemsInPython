from typing import List


cnt = 0
cnt_list: List = [0]


def test_func():
    print(f"id: {id(cnt_list)}")
    print(f"id: {id(cnt_list[0])}")
    cnt_list[0] += 1
    print(f"id: {id(cnt_list)}")
    print(f"id: {id(cnt_list[0])}")


if __name__ == "__main__":
    test_func()
