import math
import os
import random
import re
import sys


def find(user_key, master_key):
    for i in range(0, len(user_key) - len(master_key) + 1):
        for j in range(0, len(user_key[0]) - len(master_key[0]) + 1):
            if user_key[i][j:].startswith(master_key[0]):
                res = True
                for k in range(1, len(master_key)):
                    if not user_key[i+k][j:].startswith(master_key[k]):
                        res = False
                        break
                if res:
                    return True
    
    return False


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        user_key = []

        for _ in range(R):
            user_key.append(input().rstrip())

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        master_key = []

        for _ in range(r):
            master_key.append(input().rstrip())
        
        res = find(user_key, master_key)
        if res:
            print("YES")
        else:
            print("NO")