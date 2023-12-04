#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        return tuple_b
    if tuple_b == ():
        return tuple_a
    if len(tuple_a) >= 2:
        a1 = tuple_a[1]
    else:
        a1 = 0
    if len(tuple_b) >= 2:
        b1 = tuple_b[1]
    else:
        b1 = 0
    tuple_c = (tuple_a[0] + tuple_b[0], a1 + b1)
    return tuple_c


if __name__ == "__main__":
    add_tuple
