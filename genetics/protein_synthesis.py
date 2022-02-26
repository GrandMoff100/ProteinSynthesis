from dataclasses import dataclass

from .rna import RNA
from .amino_acids import AminoAcids
from typing import Generator, Tuple

class mRNA(RNA):
    def __new__(cls, code: str):
        if len(code) % 3 != 0:
            raise ValueError("Must be three-long sequences of codons.")
        return RNA.__new__(cls, code)

    @property
    def codons(self) -> Generator["Codon", None, None]:
        for i in range(0, len(self), 3):
            yield Codon(self[i : i + 3])


class Codon(mRNA):
    def __new__(cls, bases: str):
        if len(bases) != 3:
            raise ValueError(f"Codons must be three bases, got {bases.upper()}")
        return mRNA.__new__(cls, bases)

    def tRNA(self) -> "tRNA":
        return tRNA(self)
    
    @property
    def anti_codon(self) -> "Codon":
        codon = ""
        for base in self:
            if (index := RNA.bases.index(base)) % 2:
                codon += RNA.bases[index - 1]
            else:
                codon += RNA.bases[index + 1]
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
    amino_acids: Tuple[AminoAcids]
