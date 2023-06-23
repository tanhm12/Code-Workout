from typing import List
from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        res = [defaultdict(int) for i in range(n)]
        final = 1
        for i in range(1, n):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                res[i][diff] = max(res[j][diff] + 1, res[i][diff])
                final = max(final, res[i][diff])
        
        return final + 1
    
nums = [20,1,15,3,10,5,8]
nums = [9,4,7,2,10]
print(Solution().longestArithSeqLength(nums))
                
                
        