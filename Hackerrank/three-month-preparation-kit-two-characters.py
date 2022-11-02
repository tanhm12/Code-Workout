#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    from collections import defaultdict
    c2pos = defaultdict(list)
    for i in range(len(s)):
        c2pos[s[i]].append(i)
    
    res = 0
    chars = list(c2pos.keys())
    for i1 in range(len(chars)-1):
        c1 = chars[i1]
        for i2 in range(i1 +1, len(chars)):
            c2 = chars[i2]
            if c1 != c2:
                pos1 = c2pos[c1]
                pos2 = c2pos[c2]
                if 0 <= abs(len(pos1) - len(pos2)) <= 1:
                    turn = -1
                    i = 0
                    j = 0
                    while i < len(pos1) and j < len(pos2):
                        if pos1[i] < pos2[j]:
                            if turn == 1:
                                turn = -1
                                break
                            else:
                                turn = 1
                                i += 1
                        else:
                            if turn == 2:
                                turn = -1
                                break
                            else:
                                turn = 2
                                j += 1
                    print(c1, c2, i, j, turn)
                    print(pos1)
                    print(pos2)
                    if i + j + 1 == len(pos1) + len(pos2):
                        res = max(res, len(pos1) + len(pos2))
                else:
                    break
    return res

if __name__ == '__main__':

    # l = int(input().strip())

    s = input()

    result = alternate(s)

    print(result)