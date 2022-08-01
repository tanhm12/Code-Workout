from typing import List

def permuteUnique(nums: List[int]):
    from copy import deepcopy
    if len(nums) == 1:
        return [nums]
    res = []
    n = len(nums)
    
    from collections import Counter
    current_possible = dict(Counter(nums))
    current_sol = [0 for i in range(len(nums))]
    def find(i):
        for possible in current_possible:
            if current_possible[possible] > 0:
                current_possible[possible] -= 1
                current_sol[i] = possible
                if i == n - 1:
                    res.append(deepcopy(current_sol))
                else:
                    find(i+1)
                current_possible[possible] += 1
    
    find(0)
    return res

nums = [1,1,2]
nums = [1,2,3]
print(permuteUnique(nums)) 
