import math

def strangeCounter(t):
    n = int(math.log((t-1) / 3 + 1, 2))
    return 3* 2**n - (t - 3*(2**n-1) - 1)