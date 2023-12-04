#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for m in matrix:
        print(' '.join('{:d}'.format(e)for e in m))


if __name__ == "__main__":
    print_matrix_integer
