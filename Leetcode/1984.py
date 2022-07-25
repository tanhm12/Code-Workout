from typing import List

def minimumDifference(nums: List[int], k: int):
    nums.sort()
    res = nums[-1]
    for i in range(0, len(nums) - k + 1):
        res = min(res, nums[i+k-1] - nums[i])
    
    return res
    
    