#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            letter = ord(str[i]) - 32
        else:
            letter = ord(str[i])
        print("{:c}".format(letter), end="")
    print()
