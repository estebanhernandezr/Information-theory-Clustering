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