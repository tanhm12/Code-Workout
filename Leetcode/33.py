from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif target < nums[0] < nums[m]:
                l = m + 1
            elif target >= nums[0] > nums[m]:
                r = m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m
            
        return -1
                    
                
        