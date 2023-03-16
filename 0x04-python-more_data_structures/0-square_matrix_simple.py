#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_tm = []
    for itr in range(len(matrix)):
        new = []
        for itr2 in range(len(matrix[0])):
            new.append(matrix[itr][itr2] ** 2)
        matrix_tm.append(new)
    return matrix_tm
