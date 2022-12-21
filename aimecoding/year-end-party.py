#!/bin/python3

import math
import os
import random
import re
import sys

def max_beer(height):
    l = 0
    r = len(height) - 1

    cur_sol = (r - l) * min(height[l], height[r])
    while r > l:
        cur_sol = max(cur_sol, (r - l) * min(height[l], height[r]))

        if height[l] < height[r]:
            l += 1
        else:
            r -=1

    return cur_sol 

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    print(max_beer(a))
