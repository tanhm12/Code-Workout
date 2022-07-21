from typing import List

def minCost(houses: List[int], cost: List[List[int]], m: int, n: int, target: int):
    res = [[[0] * (target + 1)] * (n+1)]
    MAX_VAL = int(1e9)
    # current_neighborhood = 0
    # for i, j in enumerate(houses):
    #     res.append([[MAX_VAL] * (target + 1)] * (n+1))
    #     if j != 0:
    #         res[-1][j][] = 0
        
    for i in range(1, len(houses) + 1):
        h_index = i-1
        for j in range(n):
            for k in range(1, target + 1):
                if houses[h_index] != 0:
                    
    
    