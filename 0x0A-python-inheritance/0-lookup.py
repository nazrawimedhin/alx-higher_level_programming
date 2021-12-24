#!/usr/bin/python3
"""
A function that looks for attribute of an instance
"""
def lookup(obj):
    """Looks for attributes inside of the passed object
    
    Args:
        obj: instance of the class
        
    Returns:
        list of attribute 
    """
    return dir(obj)