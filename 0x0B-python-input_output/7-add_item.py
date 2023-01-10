#!/usr/bin/python3
"""This module adds all arguments to a Python list and save them to a file."""
<<<<<<< HEAD


import sys

=======
import sys


>>>>>>> ff355a32b71c6257aec2473ec712698179b7a139
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
