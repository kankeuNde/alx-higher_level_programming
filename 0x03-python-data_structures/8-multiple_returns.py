#!/usr/bin/python3

def multiple_returns(sentence):
    if not(sentence):
        return (0, None)
    str_len = len(sentence)
    first_char = sentence[0]
    return (str_len, first_char)
