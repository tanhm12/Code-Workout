#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input()
    
    d = "hello"
    
    for c in s:
        if c == d[0]:
            d  = d[1:]
            if len(d) == 0:
                break
    
    if len(d) == 0:
        print("YES")
    else:
        print("NO")
        
        