#!/usr/bin/python3

for l in range(ord('z'), ord('a') - 1, -1):
    if (l%2 != 0):
        letter = l -32;
    else:
        letter = l
    print("{:c}".format(letter), end="")
