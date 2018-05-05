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

    text = text.strip()

    i = 0
    while i < len(text):
        print(text[i], end="")
        if (text[i] == '?' or text[i] == '.' or text[i] == ':') and i != len - 1:
            print("\n")
            i += 1
            while text[i] == ' ' and text[i + 1] == ' ':
                i += 1
        else:
            print("\n")
            return
        i += 1
    print()
