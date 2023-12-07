#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    list_of_keys = list(a_dictionary.keys())
    list_of_keys.sort()
    new_dict = {i:a_dictionary[i] for i in list_of_keys}
    return new_dict


if __name__ == "__main__":
    print_sorted_dictionary
