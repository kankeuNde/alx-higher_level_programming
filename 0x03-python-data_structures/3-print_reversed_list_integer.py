#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    for elt in reversed(my_list):
        print("{:d}".format(elt))


if __name__ == "__main__":
    print_reversed_list_integer
