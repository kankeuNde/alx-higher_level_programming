#!/usr/bin/python3
"""
    Square class design
    """


class Square:
    """ Constructor method """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ this method compute the square area and return it"""
    def area(self):
        return self.__size ** 2
