#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def argcheck(args):
    #print(args[1])
    if len(args) == 1:
        print('''
    file not found.
    ''')
    elif len(args) > 2:
        print('''
    too many arguments.
    ''')
    else:
        brainfuck(args)

def brainfuck(args):
    if args[1] == '-h':
        print("""
    help option.
    """)

def main():
    args = sys.argv
    argcheck(args)


if __name__ == '__main__':
    main()
