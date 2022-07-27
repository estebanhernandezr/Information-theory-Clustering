import sys
sys.path.insert(0, 'python/compressors/lempel_ziv_1977/functions')
sys.path.insert(1, 'python/compressors/lempel_ziv_1977/decompressor/functions')

import math
from typing import List, Tuple
from fixed_length_codeword import decode_word
from auxiliar_functions import generate_combinations_wrapper
from reproduction_of_extension import reproduce_extension

"""
    Function: LZ77 decompressor class.
    Authors: Esteban Hernández Ramírez & Carlos Eduardo Álvarez Cabrera.

    Reference: "II. THE COMPRESSION ALGORITHM". A Universal Algorithm for Sequential Data Compression.
                IEEE TRANSACTIONS ON INFORMATION THEORY, MAY 1977. Jacob Ziv and Abraham Lempel.

    Description: Define an LZ77 decompressor given its sliding window size, lookahead buffer size, and code 
                 alphabet. Perform decompression over any given string given the decodifier parameters, as described
                 in the reference.

    Demo (usage):
            > decompresor = Decompressor(n=10, l=5, alphabet=['A', 'T', 'G', 'U'])
            > mensaje_descomprimido = decompresor.decompress('AAAAAAAATGATAAAAAAAATGAGAUTAAAAATGATAUTAAAAATGATATAGAAAATGAGTAAUAAAATGATAUTAAAAATGAGTAAGAAAATGAT', symb='_')
            > print(mensaje_descomprimido)
"""

class Decompressor:

    __symbols_to_encode = (2**16) # ASCII / UNICODE / needed to construct static dictionary of symbols

    def __init__(self, n, l, alphabet):
        self.n: int = n
        self.l: int = l
        self.alphabet = alphabet

        length: int = math.ceil(math.log(self.__symbols_to_encode, len(self.alphabet)))
        self.static_dict: List = generate_combinations_wrapper(self.alphabet, length)

    def decompress(self, coded_string: str, symb: str):
        string = (self.n-self.l)*symb

        L = math.ceil(math.log(self.n-self.l, len(self.alphabet))) + math.ceil(math.log(self.l, len(self.alphabet))) + len(self.static_dict[0])
        window_pos = 0
        i = self.n - self.l
        while (window_pos + L) <= len(coded_string):
            pos, size, char = decode_word(coded_string[window_pos : window_pos+L], self.alphabet, self.n, self.l)
            char = chr(self.static_dict.index(char))

            string += reproduce_extension(string[i-(self.n - self.l) : i], pos, size, char)
            window_pos += L
            i += size+1
        return string

decompresor = Decompressor(n=10, l=5, alphabet=['A', 'T', 'G', 'U'])
mensaje_descomprimido = decompresor.decompress('AAAAAAAATGATAAAAAAAATGAGAUTAAAAATGATAUTAAAAATGATATAGAAAATGAGTAAUAAAATGATAUTAAAAATGAGTAAGAAAATGAT', symb='_')
print(mensaje_descomprimido)