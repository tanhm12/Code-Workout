from functools import lru_cache, cache
import math
import os
import random
import re
import sys
sys.setrecursionlimit(10000)
#
# Complete the 'passwordCracker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt
#

def passwordCracker(passwords, loginAttempt):
    passwords = set(passwords)
    max_len = max([len(item) for item in passwords])
    
    @cache
    def find(position):
        if position >= len(loginAttempt):
            return []
        max_position = min(len(loginAttempt), position + max_len)
        for i in range(position+1,  max_position + 1):
            text = loginAttempt[position: i]
            if text in passwords:
                next_matches = find(i)
                if i >= len(loginAttempt):
                    return [text]
                elif len(next_matches) > 0:
                    return next_matches + [text]
                
        return []
    
    matches = find(0)
    if len(matches) > 0:
        return ' '.join(matches[::-1])
    return "WRONG PASSWORD"