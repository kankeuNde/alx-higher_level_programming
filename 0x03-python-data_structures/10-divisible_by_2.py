#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = [None] * len(my_list)
    if len(my_list) > 0:
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                new_list[i] = True
            else:
                new_list[i] = False
    return new_list


if __name__ == "__main__":
    divisible_by_2
