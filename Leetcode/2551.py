from typing import List
from queue import PriorityQueue

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        adj_sum = []
        n = len(weights)
        for i in range(n - 1):
            adj_sum.append(weights[i] + weights[i+1])
            
        adj_sum.sort()
        mx = weights[0] + weights[-1]
        mn = mx
        
        for i in range(k-1):
            mn += adj_sum[i]
            mx += adj_sum[n-2-i]
        
        return mx - mn
                