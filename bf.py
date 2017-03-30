#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# using: Python 3.5.3

import sys
import binascii

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
    with open(args[1], 'r') as f:
        line = f.readline()
        #for l in line:
        # with open('test.txt', 'wb') as g:
        #count(line)
        while line:
            #data = bytearray(line)
            #print(data)
            #with open('test.txt', 'wb') as g:
            #g.write(data)
            #g.close()
            #lineedit(line)
            #for l in line:
            #     if l == '+':
            #         d = l.replace('+', '1')
            #         g.write(ord(d))
            #print(line.rstrip())
            y = []
            for l in line:
                y.append(hex(ord(l)))
                # data = bytearray(y)
                #print(y)
                g = openwrite(data)
                g.write(data)
                # for z in y:
                #     print(z)
                #     d = bytearray(z)
                #     g.write(d)

            #g.write(d)
            line = f.readline()


#def lineedit(line):
#    #line2 = line.rstrip().replace('+','A')
#    line2 = line.rstrip().replace('+','01')
#    f.write(ch
    

def main():
    args = sys.argv
    argcheck(args)

if __name__ == '__main__':
    main()
