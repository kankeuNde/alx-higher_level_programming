#!/usr/bin/python3
"""
    Square class design
    """


class Square:
    """ Constructor method """
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    """get the size value"""
    @property
    def size(self):
        return (self.__size)

    """set the size value"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ this method compute the square area and return it"""
    def area(self):
        return self.__size ** 2

    """prints square"""
    def my_print(self):
        """ prints in the stdout the square with character #
        Args:
            none
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("\n")
