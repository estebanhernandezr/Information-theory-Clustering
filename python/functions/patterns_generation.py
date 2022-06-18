import math
import sys
sys.path.insert(1, 'python/classes/LZ77')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from typing import List

from CoderLZ77 import CoderLZ77

def repeated_seed_pattern(seed: str, reps: int):
    return (seed * reps)

def generate_random_seed(size: int, alphabet: List = ['0', '1']):
    seed: str = ''
    for i in range(0, size):
        idx = np.random.randint(len(alphabet))
        seed += alphabet[idx]
    return seed



def run(lookahead):
    n: int = 100
    m: int = 50
    window_s = []
    pattern_s = []
    compression = []
    for window_size in range(3, n):
        for pattern_size in range(1, m):
            codificador = CoderLZ77(window_size, int(np.ceil(window_size*lookahead)), ['0', '1'])
            semilla: str = generate_random_seed(pattern_size, ['0', '1'])
            patron: str = repeated_seed_pattern(semilla, 3)
            mensaje_codificado: str = codificador.codify(string=patron, symb='_')
            window_s.append(window_size)
            pattern_s.append(pattern_size)

            L = math.ceil(math.log(int(np.ceil(window_size-(window_size*lookahead))), 2)) + math.ceil(math.log(int(np.ceil(window_size*lookahead)), 2)) + 1
            compression.append(len(mensaje_codificado)/(len(patron)*L))
    return window_s, pattern_s, compression

lookahead_portion = 0.5
x, y, z = run(lookahead_portion)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z, c=z, cmap='Reds')
plt.xlabel("window size")
plt.ylabel("pattern size")
plt.title("lookahead portion: " + str(lookahead_portion))
plt.show()
