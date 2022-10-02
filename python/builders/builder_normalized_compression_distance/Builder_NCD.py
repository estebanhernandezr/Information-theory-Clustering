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
            > #sys.path.insert(1, 'python/compressors/lempel_ziv_1977/compressor')
            > from Compressor import Compressor
            > alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            > window_size = 1000
            > ahead_size = 50
            > compresor = Compressor(window_size, ahead_size, alfabeto)
            > relative_entropies = Builder()
            > relative_entropies.build(compresser=compresor, path='python\data\PDFs\\')
            > print(relative_entropies.distance_matrix)
            # [[0.9923729856070858, 0.9944642637470784, 0.9939721983023743, 0.995534140322012, 0.996678558248247, 0.9955714109976627], [0.9934801328576701, 0.9934629841477366, 0.992482431769897, 0.9960042308144318, 0.9960900844541758, 0.995260663507109], [0.9943412473859023, 0.9936264095440431, 0.9744047619047619, 0.9963567986837466, 0.9965592743196747, 0.981547619047619], [0.9945939593371724, 0.9968268891761665, 0.9967093665530614, 0.9929486426137032, 0.9962392760606417, 0.9943589140909626], [0.9950793455529585, 0.9960900844541758, 0.9954644979668439, 0.995534140322012, 0.9926493587738505, 0.9949953081013451], [0.9956944273588387, 0.9947703873181892, 0.9791666666666666, 0.9945939593371724, 0.9954644979668439, 0.9597370583401807]]
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

#sys.path.insert(1, 'python/compressors/lempel_ziv_1977/compressor')
#from Compressor import Compressor
#alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#window_size = 1000
#ahead_size = 50
#compresor = Compressor(window_size, ahead_size, alfabeto)
#relative_entropies = Builder()
#relative_entropies.build(compresser=compresor, path='python\data\PDFs\\')
#print(relative_entropies.distance_matrix)