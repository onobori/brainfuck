#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    args = sys.argv
    argcheck(args)

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
    if (args[1] == '-h') or (args[1] == '--help'):
        print("""
    help option.
    """)
    else:
        print(args[1])


if __name__ == '__main__':
    main()
