#!/usr/bin/python3
import json
"""
A function that writes
"""


def save_to_json_file(my_obj, filename):
    """ A function that writes

    Args:
        my_obj ([dict]): [python object to create the jcon file]
        filename ([json]): [json file which will be created]
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, filename)