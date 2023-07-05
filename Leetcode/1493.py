from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev1 = 0
        cur1 = 1 if nums[0] == 1 else 0
        res = 0
        for i in range(1, len(nums)):
            if nums[i] == 0:
                if nums[i-1] == 0:
                    prev1 = 0
                    cur1 =  0
                else:
                    res = max(res, cur1 + prev1)
                    prev1 = cur1
                    cur1 = 0
            else:
                cur1 += 1
        if cur1 == len(nums):
            return cur1-1
        else:
            return max(res, cur1 + prev1)