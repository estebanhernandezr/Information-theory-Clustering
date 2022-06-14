import sys
sys.path.insert(1, 'python/classes/LZ77')

import slate3k as slate
import numpy as np

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
    with open(pdf_1, 'rb') as f:
        txt_A = slate.PDF(f)

    with open(pdf_2, 'rb') as f:
        txt_B = slate.PDF(f)
    
    m = 2500
    txt_A = str(txt_A)
    txt_B = str(txt_B)
    txt_Aa = str(txt_A + txt_A[:-m])
    txt_Bb = str(txt_B + txt_B[:-m])
    txt_Ab = str(txt_A + txt_B[:-m])
    txt_Ba = str(txt_B + txt_A[:-m])
    
    dictionario = {}

    Compresor_A = CoderLZ77(n, Ls, ['0', '1'])
    Compresor_A.codify(txt_A, '_')
    dictionario['A']=len(Compresor_A.codified_string)

    Compresor_B = CoderLZ77(n, Ls, ['0', '1'])
    Compresor_B.codify(txt_B, '_')
    dictionario['B']=len(Compresor_B.codified_string)

    Compresor_Aa = CoderLZ77(n, Ls, ['0', '1'])
    Compresor_Aa.codify(txt_Aa, '_')
    dictionario['Aa']=len(Compresor_Aa.codified_string)

    Compresor_Bb = CoderLZ77(n, Ls, ['0', '1'])
    Compresor_Bb.codify(txt_Bb, '_')
    dictionario['Bb']=len(Compresor_Bb.codified_string)

    Compresor_Ab = CoderLZ77(n, Ls, ['0', '1'])
    Compresor_Ab.codify(txt_Ab, '_')
    dictionario['Ab']=len(Compresor_Ab.codified_string)

    Compresor_Ba = CoderLZ77(n, Ls, ['0', '1'])
    Compresor_Ba.codify(txt_Ba, '_')
    dictionario['Ba']=len(Compresor_Ba.codified_string)

    res = calculate2( 'Aa', 'Ab', 'Ba', 'Bb', 'A', 'B', dictionario)
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