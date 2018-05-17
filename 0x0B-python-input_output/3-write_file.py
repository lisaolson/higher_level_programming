#!/usr/bin/python3


def write_file(filename="", text=""):
    with open(filename, "r+", encoding="UTF8") as f:
        chars = f.write(text)
        return chars
