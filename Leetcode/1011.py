from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = -1
        
        l = 1
        r = sum(weights)
        while l <= r:
            m = (l+r)//2
            count  = 1
            sub_sum = 0
            for i in weights:
                if i > m:
                    count = days + 1
                sub_sum += i
                if sub_sum > m:
                    count += 1
                    sub_sum = i
            if count > days:
                l = m+1
            else:
                res = m
                r = m-1
    
        return res
        