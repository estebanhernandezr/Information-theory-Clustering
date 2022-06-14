import sys
sys.path.insert(1, 'python/classes/LZ77')
sys.path.insert(2, 'python/classes/Phylo')

from CoderLZ77 import CoderLZ77
from Phylogenetic_tree_constructor import Phylogenetic_tree

search = 2000
ahead = 1000
codificador = CoderLZ77(search, ahead, alphabet=['0', '1'])

filogenetic = Phylogenetic_tree()
filogenetic.build(codificador)