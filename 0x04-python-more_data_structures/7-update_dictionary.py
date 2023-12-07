#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    entry = {key: value}
    a_dictionary.update(entry)
    return a_dictionary


if __name__ == "__main__":
    update_dictionary
