#!/usr/bin/python3

import sys

def add_arguments():
    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)
    print(total)

add_arguments()
