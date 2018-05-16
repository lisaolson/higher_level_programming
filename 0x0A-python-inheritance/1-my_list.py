#!/usr/bin/python3
"""Module to write a class that inherits from list
"""


class MyList(list):
    """Defines MyList
    """

    def print_sorted(self):
        """Returns sorted list
        """
        print(sorted(self))
