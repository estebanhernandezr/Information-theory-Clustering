import sys
sys.path.insert(1, 'python/codifiers/codifier_lempel_ziv_1977/encoder')
sys.path.insert(2, 'python/codifiers/codifier_lempel_ziv_1977/decoder')

import matplotlib.pyplot as plt
import numpy as np

from patterns_generation import generate_random_seed, repeated_seed_pattern

from Encoder_LZ77 import Encoder as EncoderLZ77
from Decoder_LZ77 import Decoder as DecoderLZ77

"""
    TAMAÑO DE VENTANA VS TAMAÑO DEL PATRON
"""
def run(lookahead):
    n: int = 100
    m: int = 50
    window_s = []
    pattern_s = []
    compression = []
    for window_size in range(5, n):
        for pattern_size in range(1, m):
            codificador = EncoderLZ77(window_size, int(np.ceil(window_size*lookahead)), ['0', '1'])
            semilla: str = generate_random_seed(pattern_size, ['0', '1'])
            patron: str = repeated_seed_pattern(semilla, 100)
            mensaje_codificado: str = codificador.codify(string=patron, symb='_')
            window_s.append(window_size)
            pattern_s.append(pattern_size)

            compression.append(len(patron)/len(mensaje_codificado))
    return window_s, pattern_s, compression

lookahead_portion = 0.30
x, y, z = run(lookahead_portion)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z, c=z, cmap='Reds')
plt.xlabel("window size")
plt.ylabel("pattern size")
plt.title("lookahead portion: " + str(lookahead_portion))
plt.show()