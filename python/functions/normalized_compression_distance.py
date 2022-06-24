def compression_distance(x, y, compresser):
    C_xy = compresser.codify(string=(x+y), symb='_') 
    C_x = compresser.codify(string=x, symb='_')
    C_y = compresser.codify(string=y, symb='_')

    E = len(C_xy)-min(len(C_x), len(C_y))
    return E

def normalized_compression_distance(x, y, compresser):
    x = str(x)
    y = str(y)
    C_x = compresser.codify(string=x, symb='_')
    C_y = compresser.codify(string=y, symb='_')
    E = compression_distance(x, y, compresser)

    ncd = E/max(len(C_x), len(C_y))
    return ncd