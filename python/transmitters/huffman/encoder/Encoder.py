import sys
sys.path.insert(0, 'python/transmitters/huffman/functions')

from huffman_expansion import expand
from huffman_merging import merge

class Encoder:
    def __init__(self, B):
        self.B = B

    def huffman_code(self, P):
        root = merge(P, self.B)
        root = expand(root, self.B)
        return(root)