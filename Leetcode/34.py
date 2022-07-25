from typing import List

def searchRange(nums: List[int], target: int):
    if len(nums) ==0:
        return [-1, -1]
    
    
    import bisect
    
    l = bisect.bisect_left(nums, target)
    r = bisect.bisect_right(nums, target)
    print(l, r)
    
    if (l == 0 and nums[l] != target) or l == len(nums) or nums[l] != target:
        l = -1
        
    if (r == len(nums) and nums[r-1] != target) or r == 0 or nums[r-1] != target:
        r = -1 
    
    
    return [l, max(r-1, -1)]


# nums = [5,7,7,8,8,10]
# target = 8

nums = [5,7,7,8,8,10]
target = 6

# nums = [2,2]
# target = 2

print(searchRange(nums, target))
    
    