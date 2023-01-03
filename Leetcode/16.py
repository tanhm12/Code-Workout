from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            l = i+1
            r = len(nums) - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    return cur
                res = cur if abs(target - cur) < abs(target - res) else res
        
        return res

        