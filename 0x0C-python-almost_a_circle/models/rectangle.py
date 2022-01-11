#!/usr/bin/python3
"""
A Rectangle class
"""
from base import Base

class Rectangle(Base):
    """A rectangle class

    Args:
        Base ([class]): [A super class for the rectangle class]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the Rectangle class

        Args:
            width ([int]): [width of the rectangle]
            height ([int]): [height of the rectangle]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([int], optional): [description]. Defaults to None.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def X(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value
        
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """A function that calculates area of a rectangle

        Returns:
            [int]: [area of the rectangle]
        """
        return self.width * self.height