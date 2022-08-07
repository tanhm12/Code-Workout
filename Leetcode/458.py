def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int):
    T = (minutesToDie - 1) // minutesToTest + 1
    import math
    return int(math.log(buckets-1, T+1)) + 1