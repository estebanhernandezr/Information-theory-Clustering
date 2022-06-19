import sys
sys.path.insert(0, 'python/functions')

import os
import slate3k as slate

from normalized_compression_distance import normalized_compression_distance
from auxiliar_functions import lower_triangular_general
from phylogenetic_tree_visualization import visualize_phylogenetic_tree

class Clusterer:
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

                        vect.append(normalized_compression_distance(txt_A, txt_B, compresser))
                if file_1.endswith('.pdf'):
                        dictionary[file_1] = vect

        distM = [dictionary[key] for key in dictionary.keys()]
        names = [str(key)[:-4] for key in dictionary.keys()]
        distM = lower_triangular_general(distM)
        print(distM)
        visualize_phylogenetic_tree(names, distM)
        self.distance_matrix = distM