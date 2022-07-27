
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
    combinations = generate_combinations(alphabet, length, '')
    return combinations