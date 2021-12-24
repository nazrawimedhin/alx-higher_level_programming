#!/usr/bin/python3

"""
A function to check the instance of the object with the specified class
"""


def is_kind_of_class(obj, a_class):
    """[a method to check the instances of the object with the specified class]

    Args:
        obj ([object of any type]): [object to check if it's the specified class family]
        a_class ([any class]): [class to check if the class holds the specified object]

    Returns:
        [True]: [if the if the object is an instance of, or if the object is an instance of a class that inherited from]
        [False]: [otherwise]
    """
    return isinstance(obj, a_class)