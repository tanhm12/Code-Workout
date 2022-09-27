
import math

def strangeCounter_log(t):
    n = int(math.log((t-1) / 3 + 1, 2))
    x = 2**n
    return 3* x - (t - 3*(x-1) - 1)


def strangeCounter(t):
    def find_key_num(n):
        key = 1
        mul = 3
        while True:
            if key + mul <= n:
                key = key + mul
            else:
                break
            mul *= 2
        return key

    key = find_key_num(t)
    counter = key + 2
    return counter - (t - key)

import numpy as np
import timeit

t = np.random.randint(int(1e8), int(1e16), (10000,))
print(timeit.timeit(lambda: [strangeCounter_log(i) for i in t], number=10))
print(timeit.timeit(lambda: [strangeCounter(i) for i in t], number=10))