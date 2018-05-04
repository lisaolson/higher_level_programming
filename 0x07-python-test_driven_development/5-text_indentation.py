#!/usr/bin/python3
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
    for i in text:
        print(i, end="")
        if i == '?' or i == '.' or i == ':':
            print("\n")
        if i == "\n":
            print(i.lstrip())
    print()
