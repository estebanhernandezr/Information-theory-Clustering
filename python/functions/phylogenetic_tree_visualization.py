from Bio import Phylo, AlignIO
from Bio.Phylo.TreeConstruction import DistanceMatrix
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

def visualize_phylogenetic_tree(names, distM):
    distMatrix = DistanceMatrix(names=names, matrix=distM)
    constructor = DistanceTreeConstructor()
    UGMATree = constructor.upgma(distMatrix)

    Phylo.draw(UGMATree)