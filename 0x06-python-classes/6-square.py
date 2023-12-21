#!/usr/bin/python3
"""
    Square class design
    """


class Square:
    """ Constructor method """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        self.__position = position

    """get the size value"""
    @property
    def size(self):
        return (self.__size)

    """get the position value"""
    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(elt, value) for elt in value) or
                not all(elt >= 0 for elt in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print("")
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
