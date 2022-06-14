import os
import sys
sys.path.insert(1, 'python/classes/LZ77')

import slate3k as slate
import numpy as np
from Bio.Phylo.TreeConstruction import DistanceMatrix
from Bio import Phylo, AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

from CoderLZ77 import CoderLZ77

def calculate_delta(txt1, txt2, dicc):
    L1 = dicc[txt1]
    L2 = dicc[txt2]
    delta = L1 - L2
    return delta

def calculate2(Aa, Ab, Ba, Bb, A, B, dicc):
    deltaAb = calculate_delta(Ab, A, dicc)
    deltaAa = calculate_delta(Aa, A, dicc)
    deltaBa = calculate_delta(Ba, B, dicc)
    deltaBb = calculate_delta(Bb, B, dicc)
    
    return ((deltaAb - deltaBb)/deltaBb)+((deltaBa-deltaAa)/deltaAa)

def relat_entropy1(pdf_1, pdf_2, n, Ls):
    path_TXTs = 'python\data\TXTs\\'
    m = 2500
    with open(pdf_1, 'rb') as f:
        txt_A = slate.PDF(f)

    with open(pdf_2, 'rb') as f:
        txt_B = slate.PDF(f)

    txt_A = str(txt_A)
    txt_B = str(txt_B)
    txt_Aa = str(txt_A + txt_A[:-m])
    txt_Bb = str(txt_B + txt_B[:-m])
    txt_Ab = str(txt_A + txt_B[:-m])
    txt_Ba = str(txt_B + txt_A[:-m])
    
    dictionario = {}

    Compresor_A = CoderLZ77(n, Ls, ['0', '1'])
    Compresor_A.codify(txt_A, '_')
    dictionario[path_TXTs+"A.txt"]=len(Compresor_A.codified_string)

    Compresor_B = CoderLZ77(n, Ls, ['0', '1'])
    Compresor_B.codify(txt_B, '_')
    dictionario[path_TXTs+"B.txt"]=len(Compresor_B.codified_string)

    Compresor_Aa = CoderLZ77(n, Ls, ['0', '1'])
    Compresor_Aa.codify(txt_Aa, '_')
    dictionario[path_TXTs+"Aa.txt"]=len(Compresor_Aa.codified_string)

    Compresor_Bb = CoderLZ77(n, Ls, ['0', '1'])
    Compresor_Bb.codify(txt_Bb, '_')
    dictionario[path_TXTs+"Bb.txt"]=len(Compresor_Bb.codified_string)

    Compresor_Ab = CoderLZ77(n, Ls, ['0', '1'])
    Compresor_Ab.codify(txt_Ab, '_')
    dictionario[path_TXTs+"Ab.txt"]=len(Compresor_Ab.codified_string)

    Compresor_Ba = CoderLZ77(n, Ls, ['0', '1'])
    Compresor_Ba.codify(txt_Ba, '_')
    dictionario[path_TXTs+"Ba.txt"]=len(Compresor_Ba.codified_string)

    res = calculate2( path_TXTs+'Aa.txt', path_TXTs+'Ab.txt', path_TXTs+'Ba.txt', path_TXTs+'Bb.txt', path_TXTs+'A.txt', path_TXTs+'B.txt', dictionario)
    return res

def lower_triangular(matrix):
    new_filas = []
    for fila in matrix:
        new_fila = []
        for c in fila:
            new_fila.append(c)
            if c == 0:
                break
        new_filas.append(new_fila)
    return new_filas

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