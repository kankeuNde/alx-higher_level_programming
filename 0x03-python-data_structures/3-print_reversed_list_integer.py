#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0:
        for elt in reversed(my_list):
            print("{:d}".format(elt))


if __name__ == "__main__":
    print_reversed_list_integer
