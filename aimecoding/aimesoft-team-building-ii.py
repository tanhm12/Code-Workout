#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    carry = 0
    a[-1] += 1
    if a[-1] == 10:
        a[-1] = 0
        carry = 1
    for i in range(n-2, -1, -1):
        t = a[i] + carry
        if t == 10:
            a[i] = 0
            carry = 1
        else:
            a[i] = t
            carry = 0
            break
    if carry == 1:
        a = [1] + a
    
    print(" ".join(list(map(str, a))))