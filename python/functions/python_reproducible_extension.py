from typing import BinaryIO, Dict, Sequence, Tuple, List

def reproducible_extension(search: bytearray, lookahead: bytearray, n: int, Ls: int) -> Sequence[int]:
    pos: int = -1
    size: int = 0
    char: chr = ''

    for prefixsize in range(1, min(n-Ls, len(lookahead))):
        prefix: str = lookahead[ : prefixsize]
        p: int = search.rfind(prefix, 0, ((n-Ls) + prefixsize - 1))
        if p >= 0:
            pos = p
            size = prefixsize
            char = lookahead[size]
        else:
            break

    return pos, size, char

