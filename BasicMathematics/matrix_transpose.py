def transpose(matrix):
    _len_array = []
    for row in matrix:
        _len_array.append(len(row))
    if _len_array.count(_len_array[0]) != len(_len_array):
        raise RuntimeError("Invalid Matrix")
    matrix_new = []
    for column in range(len(matrix[0])):
        _new_row = []
        for row in matrix:
            _new_row.append(row[column])
        matrix_new.append(_new_row)
    return matrix_new
