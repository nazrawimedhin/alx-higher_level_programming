#!/usr/bin/python3

"""
A class inherite form a list class
"""


class MyList(list):
    """[A class inherited from list]

    Args:
        list ([class]): [super class of MyList class]
    """
    def print_sorted(self):
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)