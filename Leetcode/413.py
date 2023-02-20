from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        res = 0
        cur_diff = nums[1] - nums[0]
        cur_len = 2
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff == cur_diff:
                cur_len += 1
            else:
                cur_diff = diff
                res += (cur_len-2) * (cur_len-1) // 2
                cur_len = 2
        
        return res
        
                
        