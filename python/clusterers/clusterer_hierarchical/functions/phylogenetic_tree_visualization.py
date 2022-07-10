from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceMatrix
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

"""
    Function: Visualize distance matrix as a phylogenetic tree.
    Authors: Esteban Hernández Ramírez & Carlos Eduardo Álvarez Cabrera.
    Date: 14/06/2022

    Reference: https://biopython.org/wiki/Phylo

    Description: Build and graph a phylogenetic tree representation of a distance matrix using the
                 Unweighted pair group method with arithmetic mean for its construction.

    Demo (usage): 
            > visualize_phylogenetic_tree(['uno', 'dos', 'tres'], [[0],[1, 0],[2, 3, 0]])
            > ...
"""

def visualize_phylogenetic_tree(names, distM):
    distMatrix = DistanceMatrix(names=names, matrix=distM)
    constructor = DistanceTreeConstructor()
    UGMATree = constructor.upgma(distMatrix)

    Phylo.draw(UGMATree)