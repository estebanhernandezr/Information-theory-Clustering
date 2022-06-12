from typing import BinaryIO, Dict, Sequence, Tuple

def ini_pad(symb: int, padsize: int, cad: str) -> BinaryIO:
    pad: bytearray = bytearray(chr(symb), 'utf-8')
    for i in range(padsize-1):
        pad.append(pad[0])
    return pad + cad