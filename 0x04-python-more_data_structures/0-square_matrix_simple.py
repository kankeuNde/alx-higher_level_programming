#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for elt in matrix:
        squared_matrix.append(list(map(lambda x:x*x, elt)))
    return squared_matrix


if __name__ == "__main__":
    square_matrix_simple
