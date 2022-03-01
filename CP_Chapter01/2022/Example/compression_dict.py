import time
from functools import wraps
from typing import Dict


def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time


# try except 없을 경우 다른 경우랑 큰 차이 없음
class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    @timefn
    def _compress(self, gene: str) -> None:
        # Dictionary
        str2bit_dict: Dict[str, bin] = {"A": 0b00, "C": 0b01, "G": 0b10, "T": 0b11}

        self.bit_string: int = 1  
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            try:
                self.bit_string |= str2bit_dict[nucleotide]
            except:
                raise ValueError("Invalid nucleotide:{}".format(nucleotide))

    @timefn
    def decompress(self) -> str:
        # Dictionary
        bit2str_dict: Dict[bin, str] = {0b00: "A", 0b01: "C", 0b10: "G", 0b11: "T"}

        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = (self.bit_string >> i) & 0b11
            try:
                gene += bit2str_dict[bits]
            except:
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
    print(compressed) 
    print("Comparison b/w ORIGINAL and COMPRESSED {}".format(original == compressed.decompress()))
