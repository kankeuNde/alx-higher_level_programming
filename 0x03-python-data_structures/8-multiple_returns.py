#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    str_len = len(sentence)
    first_char = sentence[0]
    return (str_len, first_char)


if __name__ == "__main__":
    multiple_returns
