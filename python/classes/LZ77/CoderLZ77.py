import sys
sys.path.insert(0, 'python/functions')

from typing import List, Tuple
from fixed_length_codeword import codeWord
from sliding_window_mechanism import sliding_window_reproducible_extension

class CoderLZ77:

    def __init__(self, n: int, l: int):
        self.n: int = n
        self.l: int = l

    def codify(self, string: str, symb: str):
        reproducible_extensions: List[Tuple] = sliding_window_reproducible_extension(string, symb, self.n, self.l)
        for reproducible_extension in reproducible_extensions:
            pos, size, char = reproducible_extension
            print(codeWord(pos, size, char, self.n, self.l))


codificador = CoderLZ77(10, 5)
codificador.codify('aaaaaaaaaaaaaaaaaaaaaaa', 'b')