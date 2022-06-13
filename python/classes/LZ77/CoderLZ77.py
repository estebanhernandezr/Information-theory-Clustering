import sys  
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
        pad_string: str = self.__ini_search_buffer(symb, self.n-self.l, string)
        buffer: str = pad_string[: self.n]
        window_pos: int = self.n
        while window_pos - self.l < len(pad_string):
            print(buffer)
            pos, size = reproducible_extension(buffer, (self.n-self.l)-1)

            if size == 0:
                print(pos, size, buffer[(self.n-self.l)])
            elif size == min(self.l, len(buffer)-(self.n-self.l)):
                print(pos, (size-1), buffer[(self.n-self.l)+(size-1)])
            else:
                print(pos, size, buffer[(self.n-self.l)+size])
            size += 1

            if window_pos < len(pad_string):
                buffer = buffer[size : window_pos]
                buffer += pad_string[window_pos : window_pos+size]
            else:
                buffer = buffer[size :]

            window_pos += size
            
    def codify(self, string: str, symb: str):
        self.__sliding_window_mechanism(string, symb)

codificador = CoderLZ77(10, 5)
codificador.codify('bbbaaabbbaabbab', 'a')