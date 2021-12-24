#!/usr/bin/python3
def lookup(obj):
    """Looks for attributes inside of the passed object
    
    Args:
        obj: instance of the class
        
    Returns:
        list of attribute 
    """
    return list(obj.__dict__)