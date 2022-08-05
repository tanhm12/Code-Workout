from typing import List

def combinationSum4(nums: List[int], target: int):
    res = [0 for i in range(target+1)]
    
    res[0] = 1
    
    nums.sort()
    for i in range(len(res)):
        for n in nums:
            if n <= i:
                res[i] += res[i-n]
            else:
                break
    
    return res[target]



# nums = [1,2,3]
# target = 4

nums = [9]
target = 3

nums = list(range(1, 201))
target = 1000

print(combinationSum4(nums, target))

    