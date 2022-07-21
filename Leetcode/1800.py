from typing import List

def maxAscendingSum(nums: List[int]):
    res = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current_sum += nums[i]
        else:
            res = max(res, current_sum)
            current_sum = nums[i]
    
    res = max(res, current_sum)
    return res


nums = [10,20,30,40,50]
nums = [10,20,30,5,10,50]
nums = [12,17,15,13,10,11,12]
print(maxAscendingSum(nums))
    