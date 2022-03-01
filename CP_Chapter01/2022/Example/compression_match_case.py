# python > 3.10
# PEP 634 -- Structural Pattern Matching: Specification
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
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            match nucleotide:
                case "A":
                    self.bit_string |= 0b00
                case "C":
                    self.bit_string |= 0b01
                case "G":
                    self.bit_string |= 0b10
                case "T":
                    self.bit_string |= 0b11
                case _:
                    raise ValueError("Invalid nucleotide:{}".format(nucleotide))

    @timefn
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = (self.bit_string >> i) & 0b11
            match bits:
                case 0b00:
                    gene += "A"
                case 0b01:
                    gene += "C"
                case 0b10:
                    gene += "G"
                case 0b11:
                    gene += "T"
                case _:
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
