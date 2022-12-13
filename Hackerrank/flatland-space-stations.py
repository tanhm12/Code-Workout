
import math
import os
import random
import re
import sys


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    res = max(c[0] - 0, n-1-c[-1])
    for i in range(1, len(c)):
        distance = c[i] - c[i-1]-1
        if distance % 2 != 0:
            distance += 1
        res = max(distance//2, res)
    
    return res


n=6
c = list(range(n))
print(flatlandSpaceStations(n, c))
