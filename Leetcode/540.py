from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = (l+r) // 2
            if m % 2 == 0:  
                if nums[m] != nums[m+1]:
                    r = m
                else:
                    l = m+1
            else:
                if nums[m] != nums[m-1]:
                    r = m
                else:
                    l = m + 1
        return nums[l]
                
nums = [1,1,2,3,3,4,4,8,8]
nums = [1,1,2,2,3]
nums = [1,1,2,2,3,3, 4]
nums = [1,2,2,3,3, 4, 4]
nums = [1,2,2,3,3]
nums = [1,1,2,2,4,4,5,5,9]
print(Solution().singleNonDuplicate(nums))