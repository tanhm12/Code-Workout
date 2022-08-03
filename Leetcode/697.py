from typing import List

def findShortestSubArray(nums: List[int]):
    from collections import Counter
    counter = Counter(nums)
    most_commons = [counter.most_common(1)[0]]
    for item in counter.most_common(None):
        if item[1] == most_commons[0][1] and item[0] != most_commons[0][0]:
            most_commons.append(item)
            
    # print(most_commons)
    res = len(nums)
    for most_common, _ in most_commons:
        start = nums.index(most_common)
        for i in range(len(nums) - 1, start-1, -1):
            if nums[i] == most_common:
                res = min(res, i + 1 - start)
                break
    
    return res


nums = [1,2,2,3,1]
# nums= [1,2,2,3,1,4,2]

print(findShortestSubArray(nums))

