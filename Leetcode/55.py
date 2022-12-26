from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ = nums[0]
        des = len(nums) - 1 
        for i in range(1, len(nums)):
            if max_ < i :
                return False
            elif max_ >= des:
                return True
            max_ = max(max_, nums[i] + i)
        
        return True

nums = [2,3,1,1,4]
print(Solution().canJump(nums))