import sys
sys.path.insert(0, 'python/builders/builder_relative_entropy/functions/')

import os
import slate3k as slate

from relative_entropy import relat_entropy1
from auxiliar_functions import lower_triangular

"""
    Function: Phylogenetic tree class.
    Authors: Esteban Hernández Ramírez & Carlos Eduardo Álvarez Cabrera.
    Date: 14/06/2022

    Reference: None

    Description: Define a phylogenetic tree object to hold a distance matrix and generate a visualization
                 of it as a phylogenetic tree.

    Demo (usage):
            > sys.path.insert(1, 'python/compressors/lempel_ziv_1977/compressor')
            > from Compressor import Compressor
            > alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            > window_size = 10
            > ahead_size = 4
            > compresor = Compressor(window_size, ahead_size, alfabeto)
            > relative_entropies = Builder()
            > relative_entropies.build(compresser=compresor, path='python\data\PDFs\\')
            > print(relative_entropies.distance_matrix)
            # [[0.0], [0.00042120007941883657, 0.0], [0.0008268274580458643, 0.00030147454786381154, 0.0], [0.003849891258774324, 0.004287409575414082, 0.010492930923138768, 0.0], [0.007115270332232708, 0.006216573045726545, 0.018384468788876798, 0.005782709614027935, 0.0], [0.03017719319397478, 0.03749087686372641, 0.04609158835216538, 0.007553909078839925, 0.03221405440015761, 0.0]]
"""

class Builder:
    def __init__(self):
        self.labels = None
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
        #distM = lower_triangular(distM)
        self.labels = names
        self.distance_matrix = distM

#sys.path.insert(1, 'python/compressors/lempel_ziv_1977/compressor')
#from Compressor import Compressor
#alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#window_size = 1000
#ahead_size = 50
#compresor = Compressor(window_size, ahead_size, alfabeto)
#relative_entropies = Builder()
#relative_entropies.build(compresser=compresor, path='python\data\PDFs\\')
#print(relative_entropies.distance_matrix)