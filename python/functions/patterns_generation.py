import numpy as np
from typing import List

def repeated_seed_pattern(seed: str, reps: int):
    return (seed * reps)

def generate_random_seed(size: int, alphabet: List = ['0', '1']):
    seed: str = ''
    for i in range(0, size):
        idx = np.random.randint(len(alphabet))
        seed += alphabet[idx]
    return seed