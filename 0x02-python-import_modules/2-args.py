#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv_len = len(sys.argv) - 1
    if argv_len == 1:
        print("1 argument:")
    elif argv_len == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argv_len))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
