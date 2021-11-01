#!/usr/bin/env python3

import sys
args = sys.argv[1:]

VERSION = "0.0.2"

if "-v" in args or "--version" in args:
    print(VERSION)
    exit(0)

if "-h" in args or "--help" in args:
    print("This program draws a box according the numbers entered by the user.")
    print("Arguments are expected in the form label, value, label, value, etc.")
    exit(0)

if len(args) == 0:
    rows = 8
    cols = 8

if len(args) >= 1:
    cols_index = args[0]
    row_index = args[1]
    rows = int(row_index)
    cols = int(cols_index)

pos_r = rows // 2
pos_c = cols // 2

def printbox():
    for row in range(rows):
        for col in range(cols):
            if (col == 0 and row == 0) or (col == cols-1 and row == 0) or (col == 0 and row == rows-1) or (col == cols-1 and row == rows-1):
                print("+", end="")
            elif row == 0 or row == rows - 1:
                print("-", end="")
            elif col == 0 or col == cols - 1:
                print("|", end="")
            else:
                print(" ", end="")
        print()

printbox()
