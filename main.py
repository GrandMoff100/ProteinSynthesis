from genetics.cell import Ribosome
from genetics.dna import DNA

dna = DNA("ATCGGGGATTAGGCTAGCACGTGTGCCTCTATTGTCTCGGTGCTATATCGTAGCTATCTGTGC")

ribosome = Ribosome()
print(ribosome.make_protein(dna.rna()))
