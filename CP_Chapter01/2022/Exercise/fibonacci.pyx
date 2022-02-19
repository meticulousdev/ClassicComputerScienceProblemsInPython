def fib_cython(n: int) -> int:
    if n < 2:
        return 1

    ret = [0 for _ in range(n)]
    ret[0] = 1
    ret[1] = 1

    for idx in range(2, n):
        ret[idx] = ret[idx - 2] + ret[idx - 1]
    
    return ret[n - 1]