if __name__ == "__main__":
    # 1안
    trees = [-1, -1, 1, 2, 3]
    print(trees)

    cur_pos = 0
    while cur_pos < len(trees):
        if trees[cur_pos] < 0:
            del trees[cur_pos]
            continue
        cur_pos += 1
    print(trees)

    # 2안
    trees = [-1, -1, 1, 2, 3, None]
    print(trees)
    print(id(trees))
    cur_pos = 0
    while trees[cur_pos] != None:
        if trees[cur_pos] < 0:
            del trees[cur_pos]
            continue
        cur_pos += 1
    print(trees)
    print(id(trees))

    # 3안
    trees = [-1, -1, 1, 2, 3]
    trees = [tree for _, tree in enumerate(trees) if tree > 0]

    # 4안
    trees = [-1, -1, 1, 2, 3]
    print(trees)
    print(id(trees))

    for i in range(len(trees)):
        tree = trees.pop()
        if tree > 0:
            trees.insert(0, tree)

    print(trees)
    print(id(trees))
    