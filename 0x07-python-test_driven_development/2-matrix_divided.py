#!/usr/bin/python3

'''
Divide a matrix
'''


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix
    """
    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) == list:
        if len(matrix) == 0:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if not all(type(row) == list for row in matrix):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        mat = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) != float and type(matrix[i][j]) != int:
                    raise TypeError("matrix must be a matrix (list of lists)"
                                    " of integers/floats")
                row.append(round(matrix[i][j]/div, 2))
            mat.append(row)
        return mat
    else:
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
