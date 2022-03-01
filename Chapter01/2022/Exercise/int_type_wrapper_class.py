# Exercise 1.7 - 2
# title   : INT type wrapper class
# version : 2022.02.19.
# author  : kobong

# 1. int를 상속해야하나?
# 2. 순회를 어떻게 할 것인가에 대한 고민
# __next__ or __prev__ ?
# class Int (wrapper class of int)
class Int:
    def __init__(self, int_bit: int):
        self.cur = 0
        self.int_bit = int_bit
        self.len = int_bit.bit_length()

    def __iter__(self):
        return self

    # def __next__(self):
    #     if self.cur < self.len:
    #         ret = (self.int_bit >> self.cur) & 0b1
    #         self.cur += 1
    #         return ret
    #     else:
    #         raise StopIteration

    def __getitem__(self, idx: int):
        if idx < self.len:
            ret = (self.int_bit >> idx) & 0b1
            return ret
        else:
            raise IndexError


if __name__ == "__main__":
    test_Int = Int(0b0111101101011101010011)
