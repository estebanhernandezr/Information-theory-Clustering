
"""
    Function: Convert given to matrix to its lower triangular form.
    Authors: Esteban Hernández Ramírez & Carlos Eduardo Álvarez Cabrera.
    Date: 14/06/2022

    Reference:

    Description: Given a matrix as an array (rows) of arrays (columns), transform it to its lower
                 triangular form.

    Demo (usage): 
            > lower_triangular([[0, 0, 0],[1, 0, 0],[2, 3, 0]])
            > [[0], [1, 0], [2, 3, 0]]
"""

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