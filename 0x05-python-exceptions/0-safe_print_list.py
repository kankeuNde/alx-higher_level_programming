#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        printed_elts = 0
        for i in range(0, x):
            print(my_list[i], end="")
            printed_elts += 1
        print()
    except IndexError:
        print()
        return printed_elts
    return printed_elts


if __name__ == "__main__":
    safe_print_list
