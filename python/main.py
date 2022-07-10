import sys
sys.path.insert(0, 'python/functions')
sys.path.insert(1, 'python/classes/LZ77')
sys.path.insert(2, 'python/classes/Phylo')
sys.path.insert(3, 'python/classes/Clusterer')

from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np

from patterns_generation import generate_random_seed, repeated_seed_pattern

from CoderLZ77 import CoderLZ77
from NCD_Clusterer import Clusterer
from SuffixTree_CoderLZ77 import SuffixTree_CoderLZ77
from DecoderLZ77 import DecoderLZ77
from Phylogenetic_tree_constructor import Phylogenetic_tree


#alfabeto: List = ['A', 'T', 'G', 'U']
#window: int = 20
#ahead: int = 8
#mensaje: str = 'esteban hernandez ramirez aaaaaaa'

"""
    CODIFICACIÓN
"""
#codificador_iterativo = CoderLZ77(window, ahead, alfabeto)
#mensaje_codificado_iter: str = codificador_iterativo.codify(string=mensaje, symb='_')
#print(mensaje_codificado_iter)

#codificador_arbol = SuffixTree_CoderLZ77(window, ahead, alphabet=['A', 'T', 'G', 'U'])
#mensaje_codificado_arbol: str = codificador_arbol.codify(string=mensaje, symb='_')
#print(mensaje_codificado_arbol)

#print(mensaje_codificado_iter[: -10] == mensaje_codificado_arbol[: -10])

"""
    DECODIFICACIÓN
"""
#decodifier = DecoderLZ77(window, ahead, alfabeto)
#mensaje_decodificado: str = decodifier.decodify(coded_string=mensaje_codificado_arbol, symb='_')
#print(mensaje_decodificado)


"""
    ÁRBOL FILOGENÉTICO
"""
#codificador_filogenetico = CoderLZ77(300, 150, ['0', '1'])
#filogenetic = Phylogenetic_tree()
#filogenetic.build(codificador_filogenetico)


"""
    Normalized Compression Distance Clustering
"""
#sys.setrecursionlimit(1000)
#print(sys.getrecursionlimit())
#codificador_agrupador = SuffixTree_CoderLZ77(1000, 400, ['0', '1'])
#agrupador = Clusterer()
#agrupador.build(codificador_agrupador)
#print(agrupador.distance_matrix)

print("Hello world, from 'reestructuracion' branch")
codificador_agrupador = CoderLZ77(300, 150, ['0', '1'])
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