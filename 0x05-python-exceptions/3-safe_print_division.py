#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {:.1f}".format(result))
    except ZeroDivisionError:
        result = None
        print("Inside result: {}".format(result))
    finally:
        return result


if __name__ == "__main__":
    safe_print_division
