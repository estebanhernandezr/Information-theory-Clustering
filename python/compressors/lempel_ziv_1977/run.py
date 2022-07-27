import sys
sys.path.insert(0, 'python/compressors/lempel_ziv_1977/compressor')
sys.path.insert(1, 'python/compressors/lempel_ziv_1977/decompressor')

from Compressor import Compressor
from Decompressor import Decompressor

def run():
    compresor = Compressor(10, 5, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    mensaje_comprimido = compresor.compress('abababababababab', symb='_')
    print(mensaje_comprimido)

    decompresor = Decompressor(10, 5, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    mensaje_descomprimido = decompresor.decompress(mensaje_comprimido, symb='_')
    print(mensaje_descomprimido)
    
    return 0

run()