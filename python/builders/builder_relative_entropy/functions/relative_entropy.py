"""
    Function: Calculate the relative entropy between two different texts.
    Authors: Esteban Hernández Ramírez & Carlos Eduardo Álvarez Cabrera.
    Date: 14/06/2022

    Reference: Dario Benedetto, Emanuele Caglioti, and Vittorio Loreto. “Language Trees and Zipping”.
               In: Physical Review Letters 88.4 (2002). doi: 10.1103/PhysRevLett.88.048702.

    Description: Calculate the relative entropy between two text in terms of their compressed version.

    Demo (usage):
            > import sys
            > sys.path.insert(1, 'python/classes/LZ77')
            > sys.path.insert(2, 'python/classes/Phylo')
            > from CoderLZ77 import CoderLZ77
            > codificador = CoderLZ77(5, 2, alphabet=['0', '1'])
            > relat_entropy1('aaaaaaa', 'bbbbbb', codificador)
            # [3.223, 2.356]
"""

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

def relat_entropy1(txt_A, txt_B, Compresser):
    m = 2500
    txt_A = str(txt_A)
    txt_B = str(txt_B)
    txt_Aa = str(txt_A + txt_A[:-m])
    txt_Bb = str(txt_B + txt_B[:-m])
    txt_Ab = str(txt_A + txt_B[:-m])
    txt_Ba = str(txt_B + txt_A[:-m])
    
    dictionario = {}

    coded_A = Compresser.codify(txt_A, '_')
    dictionario['A']=len(coded_A)

    coded_B = Compresser.codify(txt_B, '_')
    dictionario['B']=len(coded_B)

    coded_Aa = Compresser.codify(txt_Aa, '_')
    dictionario['Aa']=len(coded_Aa)

    coded_Bb = Compresser.codify(txt_Bb, '_')
    dictionario['Bb']=len(coded_Bb)

    coded_Ab = Compresser.codify(txt_Ab, '_')
    dictionario['Ab']=len(coded_Ab)

    coded_Ba = Compresser.codify(txt_Ba, '_')
    dictionario['Ba']=len(coded_Ba)

    res = calculate2( 'Aa', 'Ab', 'Ba', 'Bb', 'A', 'B', dictionario)
    return res