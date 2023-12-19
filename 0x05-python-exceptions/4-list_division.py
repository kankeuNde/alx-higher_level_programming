#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_res_list = []
    for i in range(0, list_length):
        try:
            my_res_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            my_res_list.append(0)
            pass
        except IndexError:
            print("out of range")
            my_res_list.append(0)
            pass
        except (ValueError, TypeError):
            print("wrong type")
            my_res_list.append(0)
            pass
    return my_res_list


if __name__ == "__main__":
    list_division
