#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# using: Python 3.5.3

import sys

def argcheck(args):
    if len(args) == 1:
        print('''
    file not found.
    ''')
    elif len(args) > 2:
        print('''
    too many arguments.
    ''')
    else:
        token(args)

def token(args):
    with open(args[1], 'r') as f:
        line = f.readline()
        while line:
            y = []
            for l in line:
                y.append(l)

            print(y)
            line = f.readline()


def main():
    args = sys.argv
    argcheck(args)

if __name__ == '__main__':
    main()
