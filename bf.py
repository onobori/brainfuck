#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# using: Python 3.5.3

import sys

def argcheck(args):
    if len(args) < 2:
        print('''
    file not found.
    ''')
    elif len(args) > 3:
        print('''
    too many arguments.
    ''')
    else:
        token(args)

def token(args):
    # with open(args[1], 'rb') as f:
    with open(args[1], 'r') as f:
        # g = open(args[2], 'wb')
        line = f.readline()
        y = []
        while line:
            # y = []
            for l in line:
                y.append(l)
                # g.write(l)
                # y.append(hex(ord(l)))
                # g.write(bytes(l))
                # g.write(int(ord(l)))

            # print(y)
            line = f.readline()
        # print(y)
        parser(y)
        # print(args[2])
        # g.close()

def parser(list):
    x = []
    i = 0
    for l in list:
        if l == '+':
            i += 1
        # x.append(hex(ord(l)))
        # print(hex(ord(l)))
        elif l == '-':
            i -= 1
        elif l == '.':
            x.append(i)
            print(chr(i), end="")
            # print(chr(i), end="", file=sys.stdout)
            # sys.stdout.write(chr(i))
        elif l == ',':
            print(chr(i), end="")
        elif l == '[':
            print(chr(i), end="")
        elif l == ']':
            print(chr(i), end="")
        elif l == '>':
            print(chr(i), end="")
        elif l == '<':
            print(chr(i), end="")
        else:
            pass

    print("")
    print(x)
    # print(i)
    # print(chr(i))


if __name__ == '__main__':
    args = sys.argv
    argcheck(args)
