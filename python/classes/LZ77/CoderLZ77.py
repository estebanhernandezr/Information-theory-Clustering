import sys
sys.path.insert(0, 'python/functions')

import slate3k as slate
from typing import List, Tuple
from fixed_length_codeword import code_word
from sliding_window_mechanism import sliding_window_reproducible_extension


class CoderLZ77:

    def __init__(self, n: int, l: int, alphabet: List):
        self.n: int = n
        self.l: int = l
        self.alphabet = alphabet
        self.codified_string = ''

    def codify(self, string: str, symb: str):
        reproducible_extensions: List[Tuple] = sliding_window_reproducible_extension(string, symb, self.n, self.l)
        for reproducible_extension in reproducible_extensions:
            pos, size, char = reproducible_extension
            self.codified_string += code_word(pos, size, char, self.n, self.l, self.alphabet)