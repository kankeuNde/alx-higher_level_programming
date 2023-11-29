#!/usr/bin/python3

for letter in range(ord('z'), ord('a') - 1, -1):
    if (letter % 2 != 0):
        case_letter = letter - 32
    else:
        case_letter = letter
    print("{:c}".format(case_letter), end="")
