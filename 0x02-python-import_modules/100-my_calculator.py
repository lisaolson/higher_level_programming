#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if (len(argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] == '+':
        total = add(int(argv[1]), int(argv[3]))
    if argv[2] == '-':
        total = sub(int(argv[1]), int(argv[3]))
    if argv[2] == '*':
        total = mul(int(argv[1]), int(argv[3]))
    if argv[2] == '/':
        total = div(int(argv[1]), int(argv[3]))
    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], total))
