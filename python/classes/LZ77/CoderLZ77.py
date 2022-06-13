import sys
from typing import List  
sys.path.insert(0, 'python/functions')

from manual_reproducible_extension import reproducible_extension

class CoderLZ77:

    def __init__(self, n: int, l: int):
        self.n: int = n
        self.l: int = l
        
    def __ini_search_buffer(self, symb: int, padsize: int, cad: str) -> str:
        pad: str = symb
        for i in range(1, padsize):
            pad += symb
        return pad + cad

    def __sliding_window_mechanism(self, string: str, symb: str):
        reproducible_extensions: List = []
        pad_string: str = self.__ini_search_buffer(symb, self.n-self.l, string)
        buffer: str = pad_string[: self.n]
        window_pos: int = self.n
        while window_pos - self.l < len(pad_string):
            pos, size = reproducible_extension(buffer, (self.n-self.l)-1)

            if size == min(self.l, len(buffer)-(self.n-self.l)):
                reproducible_extensions.append((pos, size, None))
            else:
                if size == 0:
                    reproducible_extensions.append((pos, size, buffer[(self.n-self.l)]))
                else:
                    reproducible_extensions.append((pos, size, buffer[(self.n-self.l)+size]))
                size += 1

            if window_pos < len(pad_string):
                buffer = buffer[size : window_pos]
                buffer += pad_string[window_pos : window_pos+size]
            else:
                buffer = buffer[size :]

            window_pos += size
        return reproducible_extensions

    def codify(self, string: str, symb: str):
        reproducible_extensions = self.__sliding_window_mechanism(string, symb)
        print(reproducible_extensions)

codificador = CoderLZ77(10, 5)
codificador.codify('bbbaaabbbaabbab', 'a')