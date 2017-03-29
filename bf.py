#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def manual(args):
    if (args[1] == '-h') or (args[1] == '--help'):
        print("""
    help option.
    """)
    else:
        print(args[1])

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
        brainfuck(args)

def brainfuck(args):
    #manual(args)
    f = open(args[1], 'r')
    line = f.readline()
    #for l in line:
    while line:
        print(line.rstrip())
        #print(line)
        line = f.readline()
    f.close()

def count(line):
    pass

def main():
    args = sys.argv
    argcheck(args)

if __name__ == '__main__':
    main()
