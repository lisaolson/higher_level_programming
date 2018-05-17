#!/usr/bin/python3


def write_file(filename="", text=""):
    with open(filename, 'r+') as f:
        chars = f.write(text)
        return chars
