
def minMoves2(nums ):
    nums.sort()
    
    left = 0
    right = 0
    for i in range(1, len(nums)):
        right += nums[i] - nums[0]
    
    res = right
    for i in range(1, len(nums)):
        delta = nums[i] - nums[i-1]
        left +=  delta * i
        right -= delta * (len(nums) - i)
        res = min(res, left + right)
        
    return res
    

nums = [1,2,3]
nums = [1,0,0,8,6]

import random
import numpy as np
nums =  list(np.random.randint(-1000, 1000, (random.randint(0, 50),)))

print(minMoves2(nums))
print(nums)
