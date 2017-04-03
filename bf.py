#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# using: Python 3.5.3

import sys

def main(args):
    # option is unimplemented
    if len(args) < 2:
        print('''
brainfuck interpreter: ver 0.9.0
usage:
    $ python3 bf.py [option] file

sample:
    $ python3 bf.py example/hello.bf
    Brainfuck
    ''')
    elif len(args) > 3:
        print('''
    too many arguments.
    ''')
    else:
        token(args)

# 1行ずつtokenに分割してリストに保存する
def token(args):
    with open(args[1], 'r') as f:
        line = f.readline()
        list = []
        while line:
            for l in line:
                list.append(l)
            line = f.readline()
        brainfuck(list)

def brainfuck(list):
    x = []
    data = 0
    #listのインデックスをポインタとして使う
    ptr = 0
    i = 0
    for i in range(len(list)):
        if list[i] == '+':
            data += 1
        elif list[i] == '-':
            data -= 1
        elif list[i] == '.':
            x.append(data)
            print(chr(data), end="")
        elif list[i] == '>':
            x.append(0)
            ptr += 1
        elif list[i] == '<':
            ptr -= 1
        else:
            pass

    print("")


if __name__ == '__main__':
    args = sys.argv
    main(args)
