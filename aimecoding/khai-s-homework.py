#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(input())
    ori_s = s[::]
    
    l = 0
    r = len(s) - 1
    
    
    while l < r:
        if s[l] > s[r]:
            s[r] = s[l]
            k -= 1
        elif s[l] < s[r]:
            s[l] = s[r]
            k -= 1
        l += 1
        r -= 1
    
    if k < 0:
        print(-1)
        sys.exit(0)
    elif k == 0:
        print(''.join(s))
        sys.exit(0)
    elif k == 1:
        l = 0
        r = len(s) - 1
        while l < r:
            if ori_s[l] != ori_s[r] and ori_s[l] != '9' and ori_s[r] != '9':
                s[l] = '9'
                s[r] = '9'
                k -= 1
                break
            l += 1
            r -= 1
        if len(s) % 2 == 1  and k == 1:
            s[len(s) // 2] = '9'
        print(''.join(s))
        sys.exit(0)
    
    l = 0
    r = len(s) - 1
    while l <= r:
        # if s[l] != '9':
        #     s[l] = '9'
        #     s[r] = '9'
        #     k -= 2
        # l += 1
        # r -= 1
        
        if l==r:
            if k >= 1:
                s[l] = '9'
        if s[l] != '9':
            if (k >= 2 and s[l] == ori_s[l] and
                            s[r] == ori_s[r]):
                k -= 2
                s[l] = '9' 
                s[r] = '9'

            elif (k >= 1 and (s[l] != ori_s[l] or s[r] != ori_s[r])):
                k -= 1
                s[l] = '9'
                s[r] = '9'
        
        l += 1
        r -= 1
        
    print(''.join(s))


    