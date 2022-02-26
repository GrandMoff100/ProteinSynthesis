# from rich import Console
from typing import Dict, Set
from enum import Enum
from dataclasses import dataclass


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


class RNA:
    pairs: Set[str] = {"AU", "CG"}
    table: Dict[str, Dict[str, Dict[str, AminoAcids]]] = {
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


@dataclass()
class mRNA(RNA):
    code: str

    @property
    def codons(self):
        for i in range(0, len(self.code), 3):
            yield self.code[i:i+3].upper()


class tRNA(RNA):
    pass
