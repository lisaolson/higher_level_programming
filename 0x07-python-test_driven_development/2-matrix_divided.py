#!/usr/bin/python3
"""Module to return matrix of divided integers
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix: list of integers or floats
        div (int): integer or float to divide matrix by

    Raises:
        TypeError: If matrix is not list of integers or floats
        TypeError: If each row of the matrix is not the same size
        TypeError: If div is not an integer or float
        ZeroDivisionError: If div equals 0

    Returns:
        New matrix of all elements divided by div
    """
    divided = []

    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if type(matrix[0]) is tuple:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if type(matrix[1]) is tuple:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if type(matrix[0]) is dict:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if type(matrix[1]) is dict:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for j in matrix:
        for k in j:
            if type(k) is not int and type(k) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
                return
            continue

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        divided.append(list(map(lambda x: round((x / div), 2), row)))
    return divided
