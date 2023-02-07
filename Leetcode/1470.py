from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = (nums[i]<<10) | nums[i+n]
        const = (1<<10) -1
        for i in range(n-1, -1, -1):
            double_ = i << 1
            nums[double_ + 1] = nums[i] & const
            nums[double_] = nums[i]>>10
        
        return nums
