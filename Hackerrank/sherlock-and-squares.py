import math

all_squares = [i ** 2 for i in range(1, int(math.sqrt(1e9)) + 1)]

import bisect
def squares(a, b):
    start = bisect.bisect_left(all_squares, a)
    end = bisect.bisect(all_squares, b)
    
    return end - start


print(squares(9, 26))