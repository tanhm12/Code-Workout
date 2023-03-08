from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = sum(piles)
        while l < r:
            k = (l+r) // 2
            h_k = 0
            for p in piles:
                h_k += (p-1) // k + 1
                if h_k > h:
                    break
            if h_k < h:
                r = k
            else:
                l = k + 1
        
        return l
                
        
        