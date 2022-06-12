from manual_reproducible_extension import reproducible_extension

def ini_search_buffer(symb: int, padsize: int, cad: str) -> str:
    pad: str = symb
    for i in range(1, padsize):
        pad += symb
    return pad + cad

def sliding_window_mechanism(string: str, symb: str, window_size: int, lookahead_size: int):
    pad_string: str = ini_search_buffer(symb, window_size-lookahead_size, string)
    buffer: str = pad_string[: window_size]
    window_pos = window_size
    while window_pos < len(pad_string):
        

sliding_window_mechanism('bbbbbb', 'a', 5, 2)