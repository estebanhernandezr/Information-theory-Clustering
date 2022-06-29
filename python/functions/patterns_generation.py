import string
import numpy as np
from typing import List

def repeated_seed_pattern(seed: str, reps: int):
    return ((seed + '_') * reps)

def generate_random_seed(size: int, alphabet: List = ['0', '1']):
    seed: str = ''
    for i in range(0, size):
        idx = np.random.randint(len(alphabet))
        seed += alphabet[idx]
    return seed

def generate_palindrome_seed(size: int, alphabet: List = ['0', '1']):
    seed: List = ['_' for i in range(0, size, 1)]
    if size % 2 == 0:
        for i in range(0, int(size/2)):
            idx = i
            seed[i] = alphabet[idx]
            seed[len(seed)-1-i] = alphabet[idx]
        seed[int(size/2)] = alphabet[int(size/2)]
    else:
        for i in range(0, int(size/2)+1):
            idx = i
            seed[i] = alphabet[idx]
            seed[len(seed)-1-i] = alphabet[idx]
    string_seed = ''
    for i in range(len(seed)):
        string_seed += seed[i]
    return string_seed

#semilla: str = generate_palindrome_seed(10, string.ascii_lowercase)
#patron: str = repeated_seed_pattern(semilla, 2)
#print(patron)
