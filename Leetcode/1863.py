from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]):
        cache = [[0 for _ in range(33)] for _ in range(33)]
        for i in range(33):
            for j in range(i, 33):
                cache[i][j] = i^j
                cache[j][i] = cache[i][j]
        
        res = 0
        def find_combination(start, remain, prev_xor):
            nonlocal res
            if remain == 0:
                res += prev_xor
            else:
                remain -= 1
                for i in range(start, len(nums)):
                    find_combination(i+1, remain, cache[prev_xor][nums[i]])
        
        for i in range(1, len(nums)+1):
            find_combination(0, i, 0)
        
        return res

nums = [1,3]
# nums = [1,5,6]
nums = list(range(1, 13))

import numpy as np
nums = list(np.random.randint(1, 21, 12))
# nums = [20]*12

print(nums)
print(Solution().subsetXORSum(nums))
        