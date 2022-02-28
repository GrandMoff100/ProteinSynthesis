from typing import Generator, Optional, Tuple

from .amino_acids import AminoAcids
from .protein_synthesis import Protein, mRNA, tRNA


class Ribosome:
    @staticmethod
    def _assembler() -> Generator[None, Optional[tRNA], Protein]:
        amino_acids: Tuple[AminoAcids, ...] = ()
        while True:
            trna = yield None
            if trna is not None:
                if trna.amino_acid is AminoAcids.stop:
                    return Protein(amino_acids)
                amino_acids += (trna.amino_acid,)

    def make_protein(self, mrna: mRNA) -> Optional[Protein]:
        assembler = self._assembler()
        assembler.send(None)
        for trna in map(tRNA, mrna.codons):
            try:
                assembler.send(trna)
            except StopIteration as exc:
                return exc.value
        return None


class Cell:
    pass
