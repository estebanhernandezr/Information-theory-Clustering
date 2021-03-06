from typing import List

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

def lower_triangular_general(matrix):
    new_filas = []
    for i in range(0, len(matrix)):
        new_fila = []
        for j in range(0, len(matrix[i])):
            if j == i:
                new_fila.append(matrix[i][j])
                break
            else:
                new_fila.append(matrix[i][j])
        new_filas.append(new_fila)
    return new_filas

"""
    Function: Generate all combinations of symbols of the alphabet of given length.
    Authors: Esteban Hernández Ramírez & Carlos Eduardo Álvarez Cabrera.
    Date: 15/06/2022

    Reference:

    Description: Given an alphabet, and a length of the word, generate all posibles combinations of
                 the given length, of symbols of the given alphabet.

    Demo (usage): 
            > generate_combinations_wrapper(['0', '1', '2'], 2)
            > ['00', '01', '02', '10', '11', '12', '20', '21', '22']
"""

def generate_combinations(alphabet, length, combination):
    if len(combination) == length:
        return [combination]
    else:
        combinations = []
        for s in alphabet:
            combinations += generate_combinations(alphabet, length, combination+s)
        return combinations

def generate_combinations_wrapper(alphabet, length):
    combinations: List = generate_combinations(alphabet, length, '')
    return combinations

"""
    Function: Traverse the Suffix tree in post order.
    Authors: Esteban Hernández Ramírez & Carlos Eduardo Álvarez Cabrera.
    Date: 20/06/2022

    Reference:

    Description: Given a tree, traverse it in post order.

    Demo (usage):
"""

def postorder_scan_set(self):
    if self.is_leaf():
        self.new_idx = self.idx
        return self.idx

    else:
        idxs = []
        for node in self.transition_links.values():
            idxs.append(postorder_scan_set(node))

        self.new_idx = max(idxs)
        return self.new_idx