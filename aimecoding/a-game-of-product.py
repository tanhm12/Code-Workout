#!/bin/python3

import math
import os
import random
import re
import sys
from functools import lru_cache
from collections import defaultdict


x = int(input().strip())
res = defaultdict(list)
final_res = set([0])

def get_all(n):
    # print(n, final_res)
    if n in final_res:
        return 
    final_res.add(n)
    for i in range(1, int(n**0.5)+1):
        if n % i ==0:
            temp = (i-1) * (n//i+1)
            if temp not in final_res:
                get_all(temp)
            
    
    

if __name__ == '__main__':
    get_all(x)
    res = list(sorted(final_res))[:-1]
    print(len(res))
    print(" ".join(list(map(str, res))))
    