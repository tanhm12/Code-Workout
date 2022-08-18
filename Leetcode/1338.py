from typing import List

def minSetSize(arr: List[int]):
    from collections import Counter
    counter = list(Counter(arr).items())
    counter.sort(key=lambda x: x[1], reverse=True)   
    min_to_remove = len(arr) // 2
    
    res = 0
    current_sum = 0
    for x, countx in counter:
        res += 1
        current_sum +=  countx
        if current_sum >= min_to_remove:
            return res
    
    return res


def minSetSizePQ(arr: List[int]):
    from collections import Counter
    from heapq import heapify, heappop
    
    counter = [-i for i in Counter(arr).values()]
    heapify(counter)
    
    min_to_remove = len(arr) // 2
    res = 0
    current_sum = 0
    while current_sum < min_to_remove:
        res += 1
        current_sum -= heappop(counter)
    
    return res


arr = [3,3,3,3,5,5,5,2,2,7]
# arr = [7,7,7,7,7,7]

print(minSetSizePQ(arr))
    