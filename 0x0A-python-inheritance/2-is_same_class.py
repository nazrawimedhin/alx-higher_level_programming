#!/usr/bin/python3

"""
A function that checks the instance of the object 
"""


def is_same_class(obj, a_class):
    """[A function that checks the instance of the object]

    Args:
        obj ([object of any type]): [the object which will be checked]
        a_class ([a class of any type]): [the class which will be checked]

    Returns:
        [True]: [if the object is exactly an instance of the specified class]
        [False]: [if the object is not exactly an instance of the specified class]
    """
    return type(obj) is a_class