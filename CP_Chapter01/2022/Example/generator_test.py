from typing import Generator, Iterator


# Generator[YieldType, SendType, ReturnType]
def generator_y(start: int, end: int) -> Generator[int, None, None]:
    for i in range(start, end + 1):
        yield i


def generator_ys(start: int) -> Generator[int, int, None]:
    end = yield
    print(end)
    for i in range(start, end + 1):
        yield i


def generator_yr(start: int, end: int) -> Generator[int, None, str]:
    for i in range(start, end + 1):
        yield i
    
    return 'EOG'


class GeneratorWapper:
    def __init__(self, gen):
        self.gen = gen

    def __iter__(self):
        self.value = yield from self.gen


if __name__ == "__main__":
    print("Generator[int, None, None]")
    print(f"type: {type(generator_y(1, 5))}")
    print(f"return: {generator_y(1, 5)}")

    gen = generator_y(1, 5)
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))

    # https://stackoverflow.com/questions/19302530/whats-the-purpose-of-send-function-on-python-generators
    print("Generator[int, int, None]")
    gen = generator_ys(1)
    next(gen) # run up to the first yield
    gen.send(5)
    for i in gen:
        print(i)

    # https://stackoverflow.com/questions/34073370/best-way-to-receive-the-return-value-from-a-python-generator
    print("Generator[int, None, str]")
    gen = GeneratorWapper(generator_yr(1, 5))
    for i in gen:
        print(i)
    print(gen.value)
