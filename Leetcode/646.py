from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        cur = - 1e10
        res = 0
        for p1, p2 in pairs:
            if p1 > cur:
                res += 1
                cur = p2
        
        return res
