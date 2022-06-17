import sys
sys.path.insert(0, 'python/functions')

import os
import slate3k as slate

from relative_entropy import relat_entropy1
from auxiliar_functions import lower_triangular
from phylogenetic_tree_visualization import visualize_phylogenetic_tree

"""
    Function: Phylogenetic tree class.
    Authors: Esteban Hernández Ramírez & Carlos Eduardo Álvarez Cabrera.
    Date: 14/06/2022

    Reference:

    Description: Define a phylogenetic tree object to hold a distance matrix and generate a visualization
                 of it as a phylogenetic tree.

    Demo (usage):
            > import sys
            > sys.path.insert(1, 'python/classes/LZ77')
            > sys.path.insert(2, 'python/classes/Phylo')
            > from CoderLZ77 import CoderLZ77

            > codificador = CoderLZ77(200, 40, alphabet=['0', '1'])
            > filogenetic = Phylogenetic_tree()
            > filogenetic.build(codificador)
"""

class Phylogenetic_tree:
    def __init__(self):
        self.distance_matrix = None

    def build(self, compresser, path = 'python\data\PDFs\\'):
        dir_path = os.path.dirname(os.path.realpath(path))

        dictionary = {}
        for root, dirs, files in os.walk(dir_path):
            for file_1 in files:
                vect = []
                for file_2 in files:
                    if file_1.endswith('.pdf') and file_2.endswith('.pdf'):
                        with open(path+file_1, 'rb') as f:
                            txt_A = slate.PDF(f)

                        with open(path+file_2, 'rb') as f:
                            txt_B = slate.PDF(f)

                        vect.append(relat_entropy1(txt_A, txt_B, compresser))
                if file_1.endswith('.pdf'):
                        dictionary[file_1] = vect

        distM = [dictionary[key] for key in dictionary.keys()]
        names = [str(key)[:-4] for key in dictionary.keys()]
        distM = lower_triangular(distM)
        visualize_phylogenetic_tree(names, distM)
        self.distance_matrix = distM