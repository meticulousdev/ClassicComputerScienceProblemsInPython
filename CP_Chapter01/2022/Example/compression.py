import time
from functools import wraps


def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    @timefn
    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  
        # 왜 1로 시작하지? 나중에 짜르나? 
        # - 0으로 시작하면 A 같은거 안들어감
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            # bintype_bit_string = bin(self.bit_string)
            # print(bintype_bit_string)
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid nucleotide:{}".format(nucleotide))

    @timefn
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            # -1을 해줘야 처음에 넣은 1이 안들어감
            bits: int = (self.bit_string >> i) & 0b11
            # 2개씩 밀어주고 남은거를 2개 단위로 비트 연산
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof
    original: str = "AGCT" * 10
    print("ORIGINAL: {} BYTE".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print("COMPRESSED: {} BYTE".format(getsizeof(compressed.bit_string)))
    print(compressed)  # 압축해제 __str__ 실행
    print("Comparison b/w ORIGINAL and COMPRESSED {}".format(original == compressed.decompress()))
