#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    entry = {key: value}
    return a_dictionary.update(entry)


if __name__ == "__main__":
    update_dictionary
