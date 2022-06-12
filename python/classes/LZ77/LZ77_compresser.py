import sys  
sys.path.insert(0, 'python/functions')
sys.path.insert(1, 'python/metadata')

from strings_paddings import ini_pad
from import_external_files import data_from_file
from python_reproducible_extension import reproducible_extension
from typing import Sequence, Tuple
from bitarray import *


class LZ77_compresser:
    _n: int
    _Ls: int
    _symb: int
    _compressed_string: bitarray

    def __init__(self, n: int, Ls: int):
        self._n = n
        self._Ls = Ls
        self._symb = 32
        self._compressed_string = bitarray(endian='big')

    def __codify_word(self, pos: int, size: int, char: chr=None) -> str:
        n: int = self._n
        Ls: int = self._Ls
        codeword = "{0:0{width}b}".format(pos, width=len("{0:b}".format(n)))
        codeword += "{0:0{width}b}".format(size, width=len("{0:b}".format(Ls)))
        return codeword

    def __codify_cad(self, cad: str) -> None:
        n: int = self._n
        Ls: int = self._Ls
        symb: int = self._symb

        pcad: bytearray = ini_pad(symb, n-Ls, cad)
        i: int = 0
        while i < len(pcad)-(n-Ls):
            triple: Tuple = reproducible_extension(pcad[i:i+n], pcad[i+n-Ls:i+n], self._n, self._Ls)
            pos: int = triple[0]
            size: int = triple[1]
            if (pos >= 0 and size > 1):
                self._compressed_string.append(True)
                bin_code: str = self.__codify_word(pos, size)
                
                for bit in bin_code:
                    if bit == '1':
                        self._compressed_string.append(True)
                    else:
                        self._compressed_string.append(False)
                i += size
            else:
                self._compressed_string.append(False)
                self._compressed_string.frombytes(bytes([pcad[i+n-Ls]]))
                i += 1
        return None

    def compress(self, filename: str) -> None:
        filedata: bytearray = data_from_file(filename)
        self.__codify_cad(filedata)
        return None


compresor = LZ77_compresser(10, 5)
compresor.compress('python\metadata\English [UK].pdf')
print(len(compresor._compressed_string))
print("Hello world!")