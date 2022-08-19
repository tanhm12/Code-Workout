from typing import List

def isPossible(nums: List[int]):
    if len(nums) < 3: 
        return False
    from collections import Counter, defaultdict
    counter = Counter(nums)
    end = defaultdict(int)
    
    for i in nums:
        if counter[i] == 0:
            continue
        
        if end[i-1] > 0:
            end[i-1] -= 1
            counter[i] -= 1
            end[i] += 1
        elif counter[i+1] > 0 and counter[i+2] > 0:
            end[i+2] += 1
            counter[i] -= 1
            counter[i+1] -= 1
            counter[i+2] -= 1
        else:
            return False
    
    return True
            

nums = [1,2,3,3,4,4,5,5]
# nums = [1,2,3,3,4,5]
# nums = [1,2,3,4,4,5]
# nums = [1, 2, 2, 3, 3, 4,4, 5]
print(isPossible(nums))
        
        
    