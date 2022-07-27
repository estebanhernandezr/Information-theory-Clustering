import os
import sys
from typing import Dict, List
import slate3k as slate

sys.path.insert(0, 'python/builders/builder_normalized_compression_distance/functions')

from normalized_compression_distance import normalized_compression_distance

"""
    Function: Matrix builder with normalized compression distances (NCDs) as entries.
    
    Authors: Esteban Hernández Ramírez & Carlos Eduardo Álvarez Cabrera.

    Reference:

    Description: Build the NCD distance matrix with the files at given folder: default is 'python\data\PDFs\\'.

    Demo (usage):
"""

class Builder:
    def __init__(self):
        self.labels: List = None
        self.distance_matrix: List = None

    def build(self, compresser, path='python\data\PDFs\\') -> None:
        dictionary: Dict = {}
        dir_path = os.path.dirname(os.path.realpath(path))
        for root, dirs, files in os.walk(dir_path):
            for file_1 in files:
                vect: List = []
                for file_2 in files:
                    if file_1.endswith('.pdf') and file_2.endswith('.pdf'):
                        with open(path+file_1, 'rb') as f:
                            txt_A: List = slate.PDF(f)

                        with open(path+file_2, 'rb') as f:
                            txt_B: List = slate.PDF(f)

                        ncd: float = normalized_compression_distance(txt_A, txt_B, compresser) 
                        vect.append(ncd)

                if file_1.endswith('.pdf'):
                        dictionary[file_1] = vect

        distM: List = [dictionary[key] for key in dictionary.keys()]
        names: List = [str(key)[:-4] for key in dictionary.keys()]
        #distM = lower_triangular_general(distM)
        self.labels = names
        self.distance_matrix = distM