import sys
sys.path.insert(0, 'python/functions')
sys.path.insert(1, 'python/codifiers/codifier_lempel_ziv_1977/encoder')
sys.path.insert(2, 'python/codifiers/codifier_lempel_ziv_1977/decoder')
sys.path.insert(3, 'python/builders/builder_normalized_compression_distance')
sys.path.insert(4, 'python/builders/builder_relative_entropy')
sys.path.insert(5, 'python/clusterers/clusterer_hierarchical')
sys.path.insert(5, 'python/clusterers/clusterer_dimensional')

from typing import List, Tuple

from Encoder_LZ77 import Encoder as EncoderLZ77
from Decoder_LZ77 import Decoder as DecoderLZ77

from Builder_NCD import Builder as BuilderNCD
from Builder_RET import Builder as BuilderRET

from Clusterer_hierarchy import Clusterer as ClustererHierarchy
from Clusterer_dimension import Clusterer as ClustererDimension

alfabeto: List = ['A', 'T', 'G', 'U']
window: int = 500
ahead: int = 200
mensaje: str = 'esteban hernandez ramirez aaaaaaa'

"""
    ENCODE
"""
codificador_iterativo = EncoderLZ77(window, ahead, alfabeto)
mensaje_codificado_iter: str = codificador_iterativo.codify(string=mensaje, symb='_')
print(mensaje_codificado_iter)


"""
    DECODE
"""
decodifier = DecoderLZ77(window, ahead, alfabeto)
mensaje_decodificado: str = decodifier.decodify(coded_string=mensaje_codificado_iter, symb='_')
print(mensaje_decodificado)


"""
    BUILD relative entropy MATRIX
"""
#relative_entropies = BuilderRET()
#relative_entropies.build(compresser=codificador_iterativo, path='python\data\PDFs\\')
#print(relative_entropies.distance_matrix)


"""
    BUILD normalized compression distance MATRIX
"""
builderNCD = BuilderNCD()
builderNCD.build(compresser=codificador_iterativo, path='python\data\PDFs\\')
normalized_compression_distances = builderNCD.distance_matrix
print(normalized_compression_distances)


"""
    CLUSTER HIERARCHY distance matrix
"""
clusterer_hierarchy = ClustererHierarchy()
clusterer_hierarchy.clust(builderNCD.labels, normalized_compression_distances)


"""
    CLUSTER FLAT DIMENSION distance matrix
"""
#clusterer_dimension = ClustererDimension()
#clusterer_dimension.clust(builderNCD.labels, normalized_compression_distances)