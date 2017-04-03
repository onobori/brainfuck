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
    x = []
    data = 0
    #listのインデックスをポインタとして使う
    ptr = 0
    i = 0
    for i in len(list):
        count += 1
        if list[i] == '+':
            data += 1
        # x.append(hex(ord(l)))
        # print(hex(ord(l)))
        elif list[i] == '-':
            data -= 1
        elif list[i] == '.':
            x.append(data)
            print(chr(data), end="")
        # elif list[i] == ',':
        #     print(chr(data), end="")
        elif list[i] == '[':
        # # 別のリストを作成して[]内の処理を保存する
            x.append(data)
            begin = i
            if x[ptr] != 0:
                for j in range(ptr,len(list)):
                    if j == ']':
                        end = j
                        break
            else:
                i = end
                # i = end
        elif list[i] == ']':
            x.append(data)
            # end = i
            if x[ptr] == 0:
        #     if list[i] != ']':
        #         looplist.append(list[i])
        #     else:
        #         print("looplist:", end="")
        #         print(looplist)
        #     
        #     x.append(data)
        #     while x[ptr]:
        #         if l == '+':
        #             data += 1
        #         # x.append(hex(ord(l)))
        #         # print(hex(ord(l)))
        #         elif l == '-':
        #             data -= 1
        #         elif l == '.':
        #             x.append(data)
        #             print(chr(data), end="")
        #         elif l == '>':
        #             ptr += 1
        #         elif l == '<':
        #             ptr -= 1
        #         elif l == ']':
        #             if x[ptr] == 0:
        #                 break
        #             else:
        #                 continue
        #         else:
        #             pass
        #     # x.append(data)
        #     # print(x)

        #     # print(x[ptr])
        #     # print("start [")
        #     # print(x[ptr])
        #     # print(ptr)
        #     # print("end [")
        #     # while x[ptr]:
        #     #     # x[ptr] = x[ptr] - 1
        #     #     pass
        # elif l == ']':
        # x[ptr]がゼロでないなら[で保存した処理を繰り返す
        #     pass
        #     # if x[ptr] != 0:
        #     #     x[ptr] = x[ptr] - 1
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
    print("")
    #print(x)
    #print(len(x))
    # print(data)
    # print(chr(data))


if __name__ == '__main__':
    args = sys.argv
    argcheck(args)
