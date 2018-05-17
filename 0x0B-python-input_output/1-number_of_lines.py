!/usr / bin / python3


def number_of_lines(filename=""):
    with open(filename) as f:
        lineNum = 0
        for line in f:
            lineNum += 1
    return lineNum
