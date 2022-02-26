from .mixins import BasesCheck
from .protein_synthesis import mRNA


class DNA(BasesCheck):
    bases: str = "ATCG"

    def rna(self) -> mRNA:
        return mRNA(self.opposite().replace("T", "U"))

    def opposite(self) -> "DNA":
        opposite_bases = ""
        for base in self:
            if (index := self.bases.index(base)) % 2:
                opposite_bases += DNA.bases[index - 1]
            else:
                opposite_bases += DNA.bases[index + 1]
        return DNA(opposite_bases)


assert (dna := DNA("ATCGATCGATCG")).opposite().opposite() == dna
