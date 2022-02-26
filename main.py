# from rich import Console
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Generator


class AminoAcids(Enum):
    tryptophan = "Tryphonphan"
    stop = "Stop"
    cysteine = "Cysteine"
    tyrosine = "Tyrosine"
    serine = "Serine"
    leucine = "Leucine"
    phenyl_alanine = "Phenyl-Alanine"
    glycine = "Glycine"
    glutamic_acid = "Glutamic Acid"
    aspartic_acid = "Aspartic Acid"
    alanine = "Alanine"
    valine = "Valine"
    arginine = "Arginine"
    lysine = "Lysine"
    asparagine = "Asparagine"
    threonine = "Threonine"
    methionine = "Methionine"
    isoleucine = "Isoleucine"
    glutamine = "Glutamine"
    histidine = "Histidine"
    proline = "Proline"


@dataclass()
class AminoAcidLookup:
    table: Dict[str, Dict[str, Dict[str, AminoAcids]]]

    def __getitem__(self, codon: str) -> AminoAcids:
        first, second, third = codon.upper()
        return self.table[first][second][third]


class RNA:
    bases: str = "AUCG"
    amino_acids: AminoAcidLookup = AminoAcidLookup(
        {
            "A": {
                "A": {
                    "A": AminoAcids.lysine,
                    "U": AminoAcids.asparagine,
                    "C": AminoAcids.asparagine,
                    "G": AminoAcids.lysine,
                },
                "U": {
                    "A": AminoAcids.isoleucine,
                    "U": AminoAcids.isoleucine,
                    "C": AminoAcids.isoleucine,
                    "G": AminoAcids.methionine,
                },
                "C": {
                    "A": AminoAcids.threonine,
                    "U": AminoAcids.threonine,
                    "C": AminoAcids.threonine,
                    "G": AminoAcids.threonine,
                },
                "G": {
                    "A": AminoAcids.arginine,
                    "U": AminoAcids.serine,
                    "C": AminoAcids.serine,
                    "G": AminoAcids.arginine,
                },
            },
            "U": {
                "A": {
                    "A": AminoAcids.stop,
                    "U": AminoAcids.tyrosine,
                    "C": AminoAcids.tyrosine,
                    "G": AminoAcids.stop,
                },
                "U": {
                    "A": AminoAcids.leucine,
                    "U": AminoAcids.phenyl_alanine,
                    "C": AminoAcids.phenyl_alanine,
                    "G": AminoAcids.leucine,
                },
                "C": {
                    "A": AminoAcids.serine,
                    "U": AminoAcids.serine,
                    "C": AminoAcids.serine,
                    "G": AminoAcids.serine,
                },
                "G": {
                    "A": AminoAcids.stop,
                    "U": AminoAcids.cysteine,
                    "C": AminoAcids.cysteine,
                    "G": AminoAcids.tryptophan,
                },
            },
            "C": {
                "A": {
                    "A": AminoAcids.glutamine,
                    "U": AminoAcids.histidine,
                    "C": AminoAcids.histidine,
                    "G": AminoAcids.glutamine,
                },
                "U": {
                    "A": AminoAcids.leucine,
                    "U": AminoAcids.leucine,
                    "C": AminoAcids.leucine,
                    "G": AminoAcids.leucine,
                },
                "C": {
                    "A": AminoAcids.proline,
                    "U": AminoAcids.proline,
                    "C": AminoAcids.proline,
                    "G": AminoAcids.proline,
                },
                "G": {
                    "A": AminoAcids.arginine,
                    "U": AminoAcids.arginine,
                    "C": AminoAcids.arginine,
                    "G": AminoAcids.arginine,
                },
            },
            "G": {
                "A": {
                    "A": AminoAcids.glutamic_acid,
                    "U": AminoAcids.aspartic_acid,
                    "C": AminoAcids.aspartic_acid,
                    "G": AminoAcids.glutamic_acid,
                },
                "U": {
                    "A": AminoAcids.valine,
                    "U": AminoAcids.valine,
                    "C": AminoAcids.valine,
                    "G": AminoAcids.valine,
                },
                "C": {
                    "A": AminoAcids.alanine,
                    "U": AminoAcids.alanine,
                    "C": AminoAcids.alanine,
                    "G": AminoAcids.alanine,
                },
                "G": {
                    "A": AminoAcids.glycine,
                    "U": AminoAcids.glycine,
                    "C": AminoAcids.glycine,
                    "G": AminoAcids.glycine,
                },
            },
        }
    )


class Codon(str):
    def __init__(self, bases: str):
        if len(bases) != 3:
            raise ValueError(f"Codons must be three bases, got {bases.upper()}")
        if any(map(lambda x: x not in RNA.bases, bases.upper())):
            raise ValueError(f"One of these bases is not allowed: {bases.upper()}")
        super().__init__(bases.upper())

    @property
    def anti_codon(self) -> "Codon":
        codon = ""
        for base in self:
            if (index := RNA.bases.index(base)) % 2:
                codon += RNA.bases[index - 1]
            else:
                codon += RNA.bases[index + 1]
        return Codon(codon)


class mRNA(RNA):
    def __init__(self, code: str):
        if len(code) % 3 != 0:
            raise ValueError("Must be three-long sequences of codons.")
        self.code = code

    @property
    def codons(self) -> Generator[Codon, None, None]:
        for i in range(0, len(self.code), 3):
            yield Codon(self.code[i : i + 3])


class tRNA(RNA):
    def __init__(self, codon: Codon):
        self.codon = codon
        self.anti_codon = codon.anti_codon
        self.amino_acid = RNA.amino_acids[codon]


class Protein:
    pass


def Ribosome() -> Generator[None, Optiona[Codon], Protein]:
    yield None
