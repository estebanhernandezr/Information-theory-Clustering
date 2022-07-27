import sys
sys.path.insert(0, 'python/compressors/lempel_ziv_1977/functions')
sys.path.insert(1, 'python/compressors/lempel_ziv_1977/compressor/functions')

import math
from typing import List, Tuple
from fixed_length_codeword import code_word
from auxiliar_functions import generate_combinations_wrapper
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
            > compresor = Compressor(n=10, l=5, alphabet=['A', 'T', 'G', 'U'])
            > mensaje_comprimido = compresor.compress('abababababaaabbbbbabababbba', symb='_')
            > print(mensaje_comprimido)
"""

class Compressor:

    __symbols_to_encode = (2**16) # ASCII / UNICODE / needed to construct static dictionary of symbols

    def __init__(self, n: int, l: int, alphabet: List):
        self.n: int = n
        self.l: int = l
        self.alphabet: List = alphabet

        length: int = math.ceil(math.log(self.__symbols_to_encode, len(self.alphabet)))
        self.static_dict: List = generate_combinations_wrapper(self.alphabet, length)

    def compress(self, string: str, symb: str):
        reproducible_extensions: List[Tuple] = sliding_window_reproducible_extension(string, symb, self.n, self.l)
        codified_string = ''
        for reproducible_extension in reproducible_extensions:
            pos, size, char = reproducible_extension
            codified_word = code_word(pos, size, char, self.n, self.l, self.alphabet)
            codified_word = codified_word[: -1] + self.static_dict[ord(codified_word[-1])]

            codified_string += codified_word
        return codified_string

compresor = Compressor(n=10, l=5, alphabet=['A', 'T', 'G', 'U'])
mensaje_comprimido = compresor.compress('abababababaaabbbbbabababbba', symb='_')
print(mensaje_comprimido)