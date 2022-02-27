from dataclasses import dataclass
from typing import Generator, Tuple

from .amino_acids import AminoAcids
from .rna import RNA


class mRNA(RNA):
    def __new__(cls, code: str):
        if len(code) % 3 != 0:
            raise ValueError("Must be three-long sequences of codons.")
        return RNA.__new__(cls, code)

    @property
    def codons(self) -> Generator["Codon", None, None]:
        yield from map(Codon, zip(self[::3], self[1::3], self[2::3]))


class Codon(mRNA):
    def __new__(cls, bases: str):
        if len(bases) != 3:
            raise ValueError(f"Codons must be triplets, got {bases.upper()}")
        return mRNA.__new__(cls, bases)

    def tRNA(self) -> "tRNA":
        return tRNA(self)

    @property
    def anti_codon(self) -> "Codon":
        codon = ""
        for base in self:
            i = self.bases.index(base)
            codon += self.bases[i % 2::2][i % 2]
        return Codon(codon)


@dataclass()
class tRNA:
    codon: Codon

    @property
    def anti_codon(self):
        return self.codon.anti_codon

    @property
    def amino_acid(self):
        return RNA.amino_acids[self.codon]


@dataclass()
class Protein:
    amino_acids: Tuple[AminoAcids, ...]
