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
                #y.append(hex(ord(l)))
                #y.append(ord(l))
                y.append(l)
                # data = bytearray(y)
                #print(y)
                # f = openwrite(data)
                # f.write(data)
                # for z in y:
                #     print(z)
                #     d = bytearray(z)
                #     g.write(d)

            #g.write(d)
            print(y)
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
