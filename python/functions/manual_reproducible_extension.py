from typing import BinaryIO, Dict, Sequence, Tuple, List

def reproducible_extension(S: bytearray, j: int) -> Tuple:
    extensions: List[Tuple] = []

    i: int = 0
    while i <= j:
        extension: int = 1
        while ((extension <= len(S)-(j+1)) and (S[i : i+extension] == S[(j+1) : (j+1)+extension])):
            extension += 1

        extensions.append(((extension-1), i))
        i = i + 1

    longest_reproducible_extension: Tuple = max(extensions)

    pos: int = longest_reproducible_extension[1]
    size: int = longest_reproducible_extension[0]
    return (pos, size)