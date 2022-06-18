import sys
sys.path.insert(1, 'python/classes/LZ77')
sys.path.insert(2, 'python/classes/Phylo')
from typing import List, Tuple

from CoderLZ77 import CoderLZ77
from DecoderLZ77 import DecoderLZ77
from Phylogenetic_tree_constructor import Phylogenetic_tree


alfabeto: List = ['A', 'T', 'G', 'U']
window: int = 2000
ahead: int = 1000
mensaje: str = 'esteban hernandez ggghhhbabababa'

"""
    CODIFICACIÓN
"""
codificador = CoderLZ77(window, ahead, alfabeto)
mensaje_codificado: str = codificador.codify(string=mensaje, symb='_')
print(mensaje_codificado)

"""
    DECODIFICACIÓN
"""
decodifier = DecoderLZ77(window, ahead, alfabeto)
mensaje_decodificado: str = decodifier.decodify(coded_string=mensaje_codificado, symb='_')
print(mensaje_decodificado)

"""
    ÁRBOL FILOGENÉTICO
"""
filogenetic = Phylogenetic_tree()
filogenetic.build(codificador)