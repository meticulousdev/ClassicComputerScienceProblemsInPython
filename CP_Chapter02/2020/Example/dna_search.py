from enum import IntEnum
from typing import Tuple, List

# Nucleotide : variable name
# 'Nucleotide' : enumeration name
# Functional API
# The semantics of this API resemble namedtuple
Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

# Type Alias (by author)
# Q 01. Why Tuple and List?
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # Codon Type Alias
Gene = List[Codon]  # Gene Type Alias


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene

        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene


# linear search
def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False


# binary search
def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False


# DNA
gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
my_gene: Gene = string_to_gene(gene_str)

# linear search
acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))
print(acg in my_gene)

# binary search
my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))
print(binary_contains(my_sorted_gene, gat))
