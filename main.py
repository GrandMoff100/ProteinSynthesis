from genetics.dna import DNA
from genetics.cell import Ribosome


dna = DNA("ATCGGGGATTAGGCTAGCACGTGTGCCTCTATTGTCTCGGTGCTATATCGTAGCTATCTGTGC")

ribosome = Ribosome()
print(ribosome.make_protein(dna.rna()))