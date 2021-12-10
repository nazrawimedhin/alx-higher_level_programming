#!/usr/bin/python3
"""
None empty class.
"""
class Square:
    """
    A class that defines a square by its size.
    """
    def __init__(self, size=0):
        """
        Args:
            size (int) the size of a a square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Method to get the area.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Method to return the size value.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Method to set the size value of the square object.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value