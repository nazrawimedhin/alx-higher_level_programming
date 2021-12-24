def lookup(obj):
    """
    Looks for attributes inside of the passed object.
    """
    return list(obj.__dict__)