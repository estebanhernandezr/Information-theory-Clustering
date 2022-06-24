import sys
sys.path.insert(0, 'python/functions')
sys.path.insert(1, 'python/classes/SuffixTree')

import math
from typing import List, Tuple

from SuffixTree import SuffixTree

from fixed_length_codeword import code_word
from auxiliar_functions import postorder_scan_set
from auxiliar_functions import generate_combinations_wrapper
from initialization_of_search_buffer import ini_search_buffer
from suffix_tree_reproducible_extension import reproducible_extension

"""
    Function: LZ77 codifier class with suffix tree in O(n) complexity.
    Authors: Esteban Hernández Ramírez & Carlos Eduardo Álvarez Cabrera.
    Date: 13/06/2022

    Reference: "II. THE COMPRESSION ALGORITHM". A Universal Algorithm for Sequential Data Compression.
                IEEE TRANSACTIONS ON INFORMATION THEORY, MAY 1977. Jacob Ziv and Abraham Lempel.

    Description: Define an LZ77 codifier as its sliding window size, lookahead buffer size, and code alphabet.
                 Compress any given string given the codifier parameters.

    Demo (usage): 
            > codifier = CoderLZ77(n=10, l=5, alphabet=['A', 'T', 'G', 'U'])
            > codifier.codify('abababababaaabbbbbabababbba', symb='_')
            > AAAATGATAAAATGAGAUTATGATAUTATGATATAGTGAGTAAUTGATAUTATGAGTAAGTGAT
"""

class SuffixTree_CoderLZ77:

    __symbols_to_encode = 256 # ASCII / UNICODE / needed to construct static dictionary of symbols

    def __init__(self, n: int, l: int, alphabet: List):
        self.n: int = n
        self.l: int = l
        self.alphabet: List = alphabet

        length: int = math.ceil(math.log(self.__symbols_to_encode, len(self.alphabet)))
        self.static_dict: List = generate_combinations_wrapper(self.alphabet, length)

    def __sliding_window_mechanism(self, sigma, symb):
        totcode = []
        sigma = ini_search_buffer(symb, (self.n-self.l)-1, sigma)
        F = self.l
        N = self.n - self.l

        i = 0
        sigma_i = sigma[i*(N-F) : i*(N-F)+(N-1)]
        window_inf = 0
        window_sup = N-1
        while len(sigma[window_sup : window_sup + F]) > 0:
            #print(totcode)
            if i*(N-F)+(N-1) < window_sup:
                i = i + 1
                sigma_i = sigma[i*(N-F) : i*(N-F)+(N-1)]
            elif (i+1)*(N-F) <= window_sup and window_sup <= i*(N-F)+(N-1):
                S_1i = SuffixTree(sigma[(i-1)*(N-F) : (i-1)*(N-F)+(N-1)])
                S_1i.root.traverse_postorder(postorder_scan_set)
                S_i = SuffixTree(sigma_i)
                S_i1 = SuffixTree(sigma[(i+1)*(N-F) : (i+1)*(N-F)+(N-1)])

                l_1i = reproducible_extension(S_1i, sigma[window_sup : window_sup + F], lim=window_inf-(i-1)*(N-F))

                if l_1i is not None:
                    l_1i = (l_1i[0] - (window_inf-(i-1)*(N-F)), l_1i[1])

                l_i = reproducible_extension(S_i, sigma[window_sup : window_sup + F], limsup=window_sup-i*(N-F))

                l_i = (l_i[0] + (i*(N-F)-window_inf), l_i[1])
                
                l_i1 = reproducible_extension(S_i1, sigma[window_sup : window_sup + F], limsup=window_sup-(i+1)*(N-F))

                l_i1 = (l_i1[0] + ((i+1)*(N-F)-window_inf), l_i1[1])

                LIST = [(0,0), l_1i, l_i, l_i1]
                l = sorted([i for i in LIST if i is not None and i[0] < N-1], key=lambda x:x[1])[-1]

                if l[1] == 0:
                    totcode.append((0, 0, sigma[min(window_sup + l[1], len(sigma)-1)]))
                    l = (0, 0)
                else:
                    totcode.append((l[0]+1, l[1], sigma[min(window_sup + l[1], len(sigma)-1)]))

                window_inf += l[1] + 1
                window_sup += l[1] + 1
            else:
                S_1i = SuffixTree(sigma[(i-1)*(N-F) : (i-1)*(N-F)+(N-1)])
                S_1i.root.traverse_postorder(postorder_scan_set)
                S_i = SuffixTree(sigma_i)
                
                l_1i = reproducible_extension(S_1i, sigma[window_sup : window_sup + F], lim=window_inf-(i-1)*(N-F))

                if l_1i is not None:
                    l_1i = (l_1i[0] - (window_inf-(i-1)*(N-F)), l_1i[1])

                l_i = reproducible_extension(S_i, sigma[window_sup : window_sup + F], limsup=window_sup-i*(N-F))

                l_i = (l_i[0] + (i*(N-F)-window_inf), l_i[1])

                LIST = [(0,0), l_1i, l_i]
                l = sorted([i for i in LIST if i is not None and i[0] < N-1], key=lambda x:x[1])[-1]

                if l[1] == 0:
                    totcode.append((0, 0, sigma[min(window_sup + l[1], len(sigma)-1)]))
                    l = (0, 0)
                else:
                    totcode.append((l[0]+1, l[1], sigma[min(window_sup + l[1], len(sigma)-1)]))

                window_inf += l[1] + 1
                window_sup += l[1] + 1

        return totcode

    def codify(self, string: str, symb: str):
        reproducible_extensions: List[Tuple] = self.__sliding_window_mechanism(string, symb)
        print(reproducible_extensions)
        codified_string = ''
        for reproducible_extension in reproducible_extensions:
            pos, size, char = reproducible_extension
            codified_word = code_word(pos, size, char, self.n, self.l, self.alphabet)
            codified_word = codified_word[: -1] + self.static_dict[ord(codified_word[-1])]

            codified_string += codified_word
        return codified_string