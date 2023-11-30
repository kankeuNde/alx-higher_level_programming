#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv_len = len(sys.argv) -1
    res = 0

    if argv_len > 0:
        for i in range(1, len(sys.argv)):
            res += int(sys.argv[i])
    print("{}".format(res))
