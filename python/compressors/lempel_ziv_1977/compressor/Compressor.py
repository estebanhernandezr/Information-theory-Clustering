import sys
sys.path.insert(0, 'python/compressors/lempel_ziv_1977/functions')
sys.path.insert(1, 'python/compressors/lempel_ziv_1977/compressor/functions')

from block_description import block
from python_sliding_window_mechanism import sliding_window_reproducible_extension

"""
    Function: LZ77 compressor class.
    Authors: Esteban Hernández Ramírez & Carlos Eduardo Álvarez Cabrera.

    Reference: "II. THE COMPRESSION ALGORITHM". A Universal Algorithm for Sequential Data Compression.
                IEEE TRANSACTIONS ON INFORMATION THEORY, MAY 1977. Jacob Ziv and Abraham Lempel.

    Description: Define an LZ77 compressor given its sliding window size, lookahead buffer size, and code alphabet.
                 Perform compression over any given string, for the given compression parameters, as described
                 in the reference.

    Demo (usage): 
            > compresor = Compressor(10, 5, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
            > mensaje_comprimido = compresor.compress('hola mundo desde lempel ziv 1977', symb='_')
            > print(mensaje_comprimido)
"""

class Compressor:

    def __init__(self, window_size, lookahead_size, alphabet):
        self.n = window_size
        self.l = lookahead_size
        self.alpha = alphabet

    def compress(self, string, symb):
        compressed_string = []
        reproducible_extensions = sliding_window_reproducible_extension(string, symb, self.n, self.l)
        for reproducible_extension in reproducible_extensions:
            pos, size, char = reproducible_extension
            compressed_word = block(pos, size, char, self.n, self.l, self.alpha)
            compressed_string.append(compressed_word)
        return compressed_string

compresor = Compressor(10, 5, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
mensaje_comprimido = compresor.compress('hola mundo desde lempel ziv 1977', symb='_')
print(mensaje_comprimido)