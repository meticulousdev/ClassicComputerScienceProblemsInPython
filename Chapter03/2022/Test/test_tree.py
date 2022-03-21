import time


if __name__ == "__main__":
    # 1안
    num = 10000
    start = time.time()
    trees = [-1, -1, 1, 2, 3] * num
    # print(trees)

    cur_pos = 0
    while cur_pos < len(trees):
        if trees[cur_pos] < 0:
            del trees[cur_pos]
            continue
        cur_pos += 1
    # print(trees)
    print(f"data size: {len(trees)}")
    print("len")
    print(f"elapsed time: {time.time() - start:.5f}")

    # 2안
    start = time.time()
    trees = [-1, -1, 1, 2, 3] * num
    trees.append(None)
    # print(trees)
    cur_pos = 0
    while trees[cur_pos] != None:
        if trees[cur_pos] < 0:
            del trees[cur_pos]
            continue
        cur_pos += 1
    # print(trees)
    print("None")
    print(f"elapsed time: {time.time() - start:.5f}")

    # 3안
    start = time.time()
    trees = [-1, -1, 1, 2, 3] * num
    # print(trees)

    for i in range(len(trees)):
        tree = trees.pop()
        if tree > 0:
            trees.insert(0, tree)

    # print(trees)
    print("stack")
    print(f"elapsed time: {time.time() - start:.5f}")