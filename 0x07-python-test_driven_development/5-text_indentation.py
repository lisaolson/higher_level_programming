#!/usr/bin/python3
"""Module to print 2 new lines after specified characters
"""


def text_indentation(text):
    """Prints text with 2 new lines after certain characters
    Args:
        text (str): text to alternate

    Raises:
        TypeError: If text is not a string

    Returns:
        None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip()

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] == '?' or text[i] == '.' or text[i] == ':':
            print("\n")
            if text[i + 1] == ' ':
                i += 1
            if i == (len(text) - 1):
                return
            while text[i] == ' ' and text[i + 1] == ' ':
                i += 1
        i += 1
