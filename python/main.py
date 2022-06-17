import sys
sys.path.insert(1, 'python/classes/LZ77')
sys.path.insert(2, 'python/classes/Phylo')

from CoderLZ77 import CoderLZ77
from DecoderLZ77 import DecoderLZ77
from Phylogenetic_tree_constructor import Phylogenetic_tree


alfabeto = ['A', 'T', 'G', 'U']
search = 10
ahead = 4
codificador = CoderLZ77(search, ahead, alfabeto)

mensaje = 'esteban hernandez'
mensaje_codificado = codificador.codify(string=mensaje, symb='_')
print(mensaje_codificado)

decodifier = DecoderLZ77(search, ahead, alfabeto)
mensaje_decodificado = decodifier.decodify(coded_string=mensaje_codificado, symb='_')
print(mensaje_decodificado)
print('DONE')

"""
filogenetic = Phylogenetic_tree()
filogenetic.build(codificador)
"""