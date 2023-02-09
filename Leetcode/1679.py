from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter
        c = Counter(nums)
        keys = list(c.keys())
        
        res = 0
        for num in keys:
            if num not in c:
                continue
            else:
                diff = k - num
                if diff in c:
                    if diff != num :
                        res += min(c[diff], c[num])
                        del c[diff]
                    else:
                        res += c[num] // 2
                    del c[num]
                if len(c) == 0:
                    break
        return res
                    
                
            
            