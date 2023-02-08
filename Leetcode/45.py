from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        current_max = nums[0]
        next_max = nums[0]
        step = 0
        for i in range(1, len(nums)):
            if i > current_max:
                current_max = next_max
                step += 1
            if  i + nums[i] > next_max:
                next_max = i+ nums[i]
        
        return step + 1

nums = [2,3,1,1,4]
# nums = [2,3,0,1,4]

print(Solution().jump(nums))   
        
        