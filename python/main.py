import os
import sys
sys.path.insert(1, 'python/classes/LZ77')
sys.path.insert(2, 'python/classes/Phylo')

import slate3k as slate
from Bio.Phylo.TreeConstruction import DistanceMatrix
from Bio import Phylo, AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

from CoderLZ77 import CoderLZ77
from Phylogenetic_tree_constructor import relat_entropy1, lower_triangular

path: str = 'python\data\PDFs\German [Germany].pdf'
with open(path, 'rb') as f:
    txt = slate.PDF(f)
string: str = str(txt)

codificador = CoderLZ77(n=10, l=5, alphabet=['0', '1', '2', '3', '4', '5', '6'])
codificador.codify(string, symb='_')
coded_string: str = codificador.codified_string

print(len(coded_string))

search = 2000
ahead = 1000

resultados = []

path = 'python\data\PDFs\\'
dir_path = os.path.dirname(os.path.realpath(path))

PDFs = []
diccionario = {}
for root, dirs, files in os.walk(dir_path):
    for file_1 in files:
        vect = []
        for file_2 in files:
          if file_1.endswith('.pdf') and file_2.endswith('.pdf'):
              vect.append(relat_entropy1(path+file_1, path+file_2, search, ahead))
        if file_1.endswith('.pdf'):
            diccionario[file_1] = vect

distM = [diccionario[key] for key in diccionario.keys()]
nombres = [str(key)[:-4] for key in diccionario.keys()]
distM = lower_triangular(distM)


distMatrix = DistanceMatrix(names=nombres, matrix=distM)
constructor = DistanceTreeConstructor()
UGMATree = constructor.upgma(distMatrix)

Phylo.draw(UGMATree)