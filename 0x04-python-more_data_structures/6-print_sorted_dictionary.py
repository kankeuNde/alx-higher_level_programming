#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        for entry in sorted(list(a_dictionary.keys())):
            print('{}: {}'.format(entry, a_dictionary[entry]))


if __name__ == "__main__":
    print_sorted_dictionary
