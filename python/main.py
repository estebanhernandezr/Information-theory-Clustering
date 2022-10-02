import sys
sys.path.insert(0, 'python/functions')
sys.path.insert(1, 'python/compressors/lempel_ziv_1977/compressor')
sys.path.insert(2, 'python/compressors/lempel_ziv_1977/decompressor')
sys.path.insert(3, 'python/transmitters/hartley/encoder')
sys.path.insert(4, 'python/transmitters/hartley/decoder')
sys.path.insert(5, 'python/builders/builder_relative_entropy')
sys.path.insert(6, 'python/builders/builder_normalized_compression_distance')
sys.path.insert(7, 'python\clusterers\clusterer_dimensional')
sys.path.insert(8, 'python\clusterers\clusterer_hierarchical')

from Compressor import Compressor
from Decompressor import Decompressor
from Encoder import Encoder
from Decoder import Decoder
from Builder_RET import Builder as BuilderRET
from Builder_NCD import Builder as BuilderNCD
from Clusterer_dimension import Clusterer as ClustererDimension
from Clusterer_hierarchy import Clusterer as ClustererHierarchy

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
window_size = 1000
ahead_size = 200
mensaje: str = 'estebanhernandezramirezaaaaaaa'

"""
    COMPRESS
"""
compresor = Compressor(window_size, ahead_size, alfabeto)
#mensaje_comprimido = compresor.compress(mensaje, symb='_')
#print(mensaje_comprimido)

#flujo_comprimido = ''
#for block in mensaje_comprimido:
#    flujo_comprimido += block

"""
    ENCODE
"""

#codificador = Encoder(alfabeto, alfabeto)
#flujo_codificado = codificador.encode(flujo_comprimido)
#print(flujo_codificado)

"""
    DECODE
"""
#decodificador = Decoder(alfabeto, alfabeto)
#flujo_decodificado = decodificador.decode(flujo_codificado)
#print(flujo_decodificado)
#bloques = []
#block_size = len(mensaje_comprimido[0])
#pos = 0
#while (pos + block_size) <= len(flujo_decodificado):
#    bloques.append(flujo_decodificado[pos : pos + block_size])
#    pos += block_size

"""
    DECOMPRESS
"""
#decompresor = Decompressor(10, 5, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
#mensaje_descomprimido = decompresor.decompress(bloques, symb='_')
#print(mensaje_descomprimido)

"""
    BUILD relative entropy MATRIX
"""
print("RELATIVE ENTROPY DISTANCE")
builder_ret = BuilderRET()
builder_ret.build(compresser=compresor, path='python\data\PDFs\\')
relative_entropy_distances = builder_ret.distance_matrix
print(relative_entropy_distances)

"""
    BUILD normalized compression distance MATRIX
"""
print("NORMALIZED COMPRESSION DISTANCE")
builder_ncd = BuilderNCD()
builder_ncd.build(compresser=compresor, path='python\data\PDFs\\')
normalized_compression_distances = builder_ncd.distance_matrix
print(normalized_compression_distances)

"""
    CLUSTER HIERARCHY distance matrix
"""
#clusterer_hierarchy = Clusterer()
#clusterer_hierarchy.clust(builderNCD.labels, normalized_compression_distances)

"""
    CLUSTER FLAT DIMENSION distance matrix
"""
clusterer_dimension = ClustererHierarchy()
clusterer_dimension.clust(builder_ret.labels, relative_entropy_distances)

clusterer_dimension = ClustererHierarchy()
clusterer_dimension.clust(builder_ncd.labels, normalized_compression_distances)

