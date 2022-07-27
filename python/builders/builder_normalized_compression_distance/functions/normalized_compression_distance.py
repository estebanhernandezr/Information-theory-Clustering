"""
    Function: Normalized compression distance.
    
    Authors: Esteban Hernández Ramírez & Carlos Eduardo Álvarez Cabrera.

    Reference:

    Description: Compute the Normalized Compression Distance between two given strings, x and y, compressing
                 with some given compresser.

    Demo (usage):
            > normalized_compression_distance('abababababababa', 'cabbabcabcababc', CoderLZ77(6, 2, ['0', '1']))
"""

def normalized_compression_distance(x: str, y: str, compresser) -> float:
    # pre processing
    x: str = str(x)[: -500]
    y: str = str(y)[: -500]

    # compressed files
    C_xy: str = compresser.codify(string=(x+y), symb='_') 
    C_x: str = compresser.codify(string=x, symb='_')
    C_y: str = compresser.codify(string=y, symb='_')
    
    # compression distance
    E: float = len(C_xy) - min(len(C_x), len(C_y))

    # normalized compression distance
    NCD: float = E / max(len(C_x), len(C_y))
    return NCD