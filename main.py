from genetics.rna import RNA
from genetics.dna import DNA
from genetics.cell import Ribosome


if __name__ == "__main__":
    dna = DNA("TTCCTCTGGATGCTCCTGGTTAATCTCCTATGG aaa aaa cca tgg gag taa aac".replace(' ', ''))
    ribosome = Ribosome()
    rna = dna.opposite().rna()
    print(*ribosome.make_protein(rna).amino_acids, sep="\n\n")


while True:
    print(repr(RNA.amino_acids[input("Lookup: ").strip()[0:3]]))
