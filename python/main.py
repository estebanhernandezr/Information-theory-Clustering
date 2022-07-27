import sys
sys.path.insert(0, 'python/functions')
sys.path.insert(1, 'python/compressors/lempel_ziv_1977/compressor')
sys.path.insert(2, 'python/compressors/lempel_ziv_1977/decompressor')
sys.path.insert(3, 'python/transmitters/hartley/encoder')
sys.path.insert(4, 'python/transmitters/hartley/decoder')

from Compressor import Compressor
from Decompressor import Decompressor
from Encoder import Encoder
from Decoder import Decoder

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
window_size = 10
ahead_size = 4
mensaje: str = 'esteban hernandez ramirez aaaaaaa'

"""
    COMPRESS
"""
compresor = Compressor(10, 5, alfabeto)
mensaje_comprimido = compresor.compress('abababababababab', symb='_')
print(mensaje_comprimido)

flujo_comprimido = ''
for block in mensaje_comprimido:
    flujo_comprimido += block

"""
    ENCODE
"""

codificador = Encoder(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1'])
flujo_codificado = codificador.encode(flujo_comprimido)

print(flujo_codificado)
"""
    DECODE
"""
decodificador = Decoder(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1'])
flujo_decodificado = decodificador.decode(flujo_codificado)

bloques = []
block_size = len(mensaje_comprimido[0])
pos = 0
while (pos + block_size) <= len(flujo_decodificado):
    bloques.append(flujo_decodificado[pos : pos + block_size])
    pos += block_size

"""
    DECOMPRESS
"""
decompresor = Decompressor(10, 5, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
mensaje_descomprimido = decompresor.decompress(bloques, symb='_')
print(mensaje_descomprimido)

"""
    BUILD relative entropy MATRIX
"""
#relative_entropies = BuilderRET()
#relative_entropies.build(compresser=codificador_iterativo, path='python\data\PDFs\\')
#print(relative_entropies.distance_matrix)


"""
    BUILD normalized compression distance MATRIX
"""
#builderNCD = BuilderNCD()
#builderNCD.build(compresser=codificador_iterativo, path='python\data\PDFs\\')
#normalized_compression_distances = builderNCD.distance_matrix
#print(normalized_compression_distances)


"""
    CLUSTER HIERARCHY distance matrix
"""
#clusterer_hierarchy = ClustererHierarchy()
#clusterer_hierarchy.clust(builderNCD.labels, normalized_compression_distances)


"""
    CLUSTER FLAT DIMENSION distance matrix
"""
#clusterer_dimension = ClustererDimension()
#clusterer_dimension.clust(builderNCD.labels, normalized_compression_distances)