#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# using: Python 3.5.3

import sys

# x = []
# i = 0
# #listのインデックスをポインタとして使う
# ptr = 0

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
        list = []
        while line:
            # list = []
            for l in line:
                list.append(l)
                # g.write(l)
                # list.append(hex(ord(l)))
                # g.write(bytes(l))
                # g.write(int(ord(l)))

            # print(list)
            line = f.readline()
        # print(y)
        calc(list)
        # print(args[2])
        # g.close()

# def main(l):
#     pass
# 
# def loop(l):
#     if (l == '[') and (l != ']'):
#         calc(l)
#     elif (l != '[') and (l == ']'):
#         pass
# 

def calc(list):
    x = ['0']
    data = 0
    ptr = 0
    begin = 0
    end = 0
    i = 0
    for i in range(len(list)):
        if list[i] == '+':
            data += 1
        elif list[i] == '-':
            data -= 1
        elif list[i] == '.':
            x[ptr] = data
            print(chr(data), end="")
        elif list[i] == '[':
            x[ptr] = data
            begin = i
            looplist = []
            if x[ptr] != 0:
                for j in range(begin+1,len(list)):
                    if list[j] != ']' and end <= j:
                        looplist.append(list[j])
                    elif list[j] == ']' and end <= j:
                        end = j
                    elif list[j] == ']' and end > j:
                        pass
            else:
                # unimplemented
                pass

        elif list[i] == ']':
            x[ptr] = data
            while x[ptr] != 0:
                # calc(looplist)
                for k in range(len(looplist)):
                    if looplist[k] == '+':
                        data += 1
                    elif looplist[k] == '-':
                        data -= 1
                    elif looplist[k] == '.':
                        x[ptr] = data
                        print(chr(data), end="")
                    elif looplist[k] == '>':
                        x.append(0)
                        ptr += 1
                    elif looplist[k] == '<':
                        ptr -= 1
                    else:
                        pass
        elif list[i] == '>':
            x.append(0)
            ptr += 1
        elif list[i] == '<':
            ptr -= 1
        else:
            pass

    print("")
    # print("looplist:", end="")
    # print(looplist)
    # print(list)
    print(begin, end="")
    print("")
    print(end, end="")
    print("")
    #print(x)
    #print(len(x))
    # print(data)
    # print(chr(data))


if __name__ == '__main__':
    args = sys.argv
    argcheck(args)
