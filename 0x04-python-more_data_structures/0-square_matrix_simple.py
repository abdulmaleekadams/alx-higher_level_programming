#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    A function that computes the square
    value of all integers of a matrix.
    """
    square_matrix = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        square_matrix.append(result)
    return square_matrix
