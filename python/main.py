import sys
sys.path.insert(1, 'python/functions')
sys.path.insert(1, 'python/classes/LZ77')
sys.path.insert(2, 'python/classes/Phylo')
sys.path.insert(3, 'python/classes/Clusterer')

from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np

from patterns_generation import generate_random_seed, repeated_seed_pattern

from CoderLZ77 import CoderLZ77
from NCD_Clusterer import Clusterer
from DecoderLZ77 import DecoderLZ77
from Phylogenetic_tree_constructor import Phylogenetic_tree


#alfabeto: List = ['A', 'T', 'G', 'U']
#window: int = 2000
#ahead: int = 1000
#mensaje: str = 'esteban hernandez ggghhhbabababa'

"""
    CODIFICACIÓN
"""
#codificador = CoderLZ77(window, ahead, alfabeto)
#mensaje_codificado: str = codificador.codify(string=mensaje, symb='_')
#print(mensaje_codificado)


"""
    DECODIFICACIÓN
"""
#decodifier = DecoderLZ77(window, ahead, alfabeto)
#mensaje_decodificado: str = decodifier.decodify(coded_string=mensaje_codificado, symb='_')
#print(mensaje_decodificado)


"""
    ÁRBOL FILOGENÉTICO
"""
#codificador_filogenetico = CoderLZ77(2000, 1000, ['0', '1'])
#filogenetic = Phylogenetic_tree()
#filogenetic.build(codificador)


"""
    Normalized Compression Distance Clustering
"""
codificador_agrupador = CoderLZ77(5000, 2000, ['0', '1'])
agrupador = Clusterer()
agrupador.build(codificador_agrupador)
print(agrupador.distance_matrix)

"""
    TAMAÑO DE VENTANA VS TAMAÑO DEL PATRON
"""
#def run(lookahead):
#    n: int = 100
#    m: int = 50
#    window_s = []
#    pattern_s = []
#    compression = []
#    for window_size in range(5, n):
#        for pattern_size in range(1, m):
#            codificador = CoderLZ77(window_size, int(np.ceil(window_size*lookahead)), ['0', '1'])
#            semilla: str = generate_random_seed(pattern_size, ['0', '1'])
#            patron: str = repeated_seed_pattern(semilla, 100)
#            mensaje_codificado: str = codificador.codify(string=patron, symb='_')
#            window_s.append(window_size)
#            pattern_s.append(pattern_size)
#
#            compression.append(len(patron)/len(mensaje_codificado))
#    return window_s, pattern_s, compression
#
#lookahead_portion = 0.30
#x, y, z = run(lookahead_portion)
#
#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.scatter3D(x, y, z, c=z, cmap='Reds')
#plt.xlabel("window size")
#plt.ylabel("pattern size")
#plt.title("lookahead portion: " + str(lookahead_portion))
#plt.show()
