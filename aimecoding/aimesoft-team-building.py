#!/bin/python3

import math
import os
import random
import re
import sys


def cal_sol(a,x,b, n):
    if (n-a*x)  % b == 0:
        return True, (n-a*x)  // b
    else:
        return False, -1
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    a = int(first_multiple_input[1])

    b = int(first_multiple_input[2])
    
    for i in range(n+1):
        a1, a2 = cal_sol(a, i, b, n)
        if a[1]:
            print(i + a2)
            sys.exit(0)
    
    print(-1)
            
    
