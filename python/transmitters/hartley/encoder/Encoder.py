import sys
sys.path.insert(0, 'python/transmitters/hartley/functions')

import numpy as np

from fixed_length_code import generate_combinations_wrapper

class Encoder:
    def __init__(self, source_alphabet, channel_alphabet):
        self.alpha_A = source_alphabet
        self.alpha_B = channel_alphabet
        self.codewords = None
        self.build_codewords()

    def build_codewords(self):
        codeword_len = int(np.ceil(np.log(len(self.alpha_A)) / np.log(len(self.alpha_B))))
        codewords = generate_combinations_wrapper(self.alpha_B, codeword_len)
        self.codewords = codewords

    def encode(self, string):
        codified_string = ''
        for a in string:
            idx = self.alpha_A.index(a)
            codified_string += self.codewords[idx]
        return codified_string

#codificador = Encoder(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1'])
#print(codificador.encode('abbac9'))