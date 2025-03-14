
from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies.sort(reverse=True)
        
        def verify(cand: int):
            if cand == 0: return True
            tgt = k
            
            for num in candies:
                if num < cand:
                    break
                tgt -= num // cand
                if tgt <= 0:
                    return True
            
            return tgt <= 0
        
        l = 0
        r = sum(candies) // k
        while l < r:
            m = (l+r) // 2
            if verify(m):
                l = m+1
            else:
                r = m
        
        return l if verify(l) else l-1
    

