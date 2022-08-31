from typing import List

class Solution:
    def canPartition(self, nums: List[int]):
        summ = sum(nums)
        if summ % 2 != 0 :
            return False
        else:
            target = summ//2
            res = [[False for i in range(target + 1)] for j in range(len(nums) + 1)]
            
            for i in range(len(nums)):
                res[i][0] = True
                for j in range(target + 1):
                    if res[i][j]:
                        res[i+1][j] = True
                        next_target = j + nums[i]
                        if next_target <= target:
                            res[i+1][next_target] = True
            
            return res[-1][target]
        
        
nums = [1,5,11,5]
nums = [1,2,3,5]
# nums = [1,2,3,4]

# import numpy as np
# nums = list(np.random.randint(1, 101, (np.random.randint(0, 201), )))

# nums = [14,9,8,4,3,2]
print(nums)
print(Solution().canPartition(nums))
        
        