import math
import os
import random
import re
import sys


def commonChild(s1, s2):
    final_res = 0
    res = [[0 for i in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                res[i][j] = res[i-1][j-1] + 1
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1])
            final_res = max(res[i][j], final_res)
    
    return final_res
    
            
if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(result)