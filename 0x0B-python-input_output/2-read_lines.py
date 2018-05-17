#!/usr/bin/python3

def read_lines(filename="", nb_lines=0):
    with open(filename) as f:
        lineNum = 0
        for line in f:
            lineNum += 1
        if nb_lines >= lineNum or nb_lines <= 0:
            f.seek(0, 0)
            print(f.read())
        else:
            lineNum = 0
            f.seek(0, 0)
            while (lineNum < nb_lines):
                print(f.readline())
                lineNum += 1
