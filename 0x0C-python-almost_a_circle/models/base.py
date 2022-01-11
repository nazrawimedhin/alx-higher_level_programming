#!/usr/bin/python3
"""
This is a base class for the project
"""
class Base:
    """
    Base class for this project
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """construction of the class

        Args:
            id ([int], optional): [a number holding some id value]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects