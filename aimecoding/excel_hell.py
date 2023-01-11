#!/bin/python3

import math
import os
import random
import re
import sys
import string

def divmod_excel(n):
    a, b = divmod(n, 26)
    if b == 0:
        return a - 1, b + 26
    return a, b

def to_excel(num):
    chars = []
    while num > 0:
        num, d = divmod_excel(num)
        chars.append(string.ascii_uppercase[d - 1])
    return ''.join(reversed(chars))

if __name__ == '__main__':
    n = int(input().strip())
    print(to_excel(n))