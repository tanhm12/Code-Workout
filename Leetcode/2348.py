from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        from collections  import defaultdict
        count = defaultdict(int)
        
        cur_len = 0
        for i in nums:
            if i == 0:
                cur_len += 1
            else:
                count[cur_len] += 1
                cur_len = 0
        
        if cur_len != 0:
            count[cur_len] += 1
        
        res = 0
        for length in count:
            freq = count[length]
            res += freq * length * (length+1) // 2
        
        return res 
        
        