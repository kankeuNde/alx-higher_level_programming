#!/usr/bin/python3

def remove_char_at(str, n):
    word = str
    if n >= 0:
        word = str[0:n] + str[n+1:]
    return word
