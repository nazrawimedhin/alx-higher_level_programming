#!/usr/bin/python3
"""
A function which reads a file
"""
def read_file(filename=""):
    """A function which reads a file

    Args:
        filename (str): [the file that will be readed by th function].
    """
    with open("filename", encoding="utf-8", mode="r") as my_file:
        my_file = filename.read()
        print(my_file)