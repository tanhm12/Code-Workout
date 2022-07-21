import time

def isPossible(target):
    n = len(target)
    # count_1 = 0
    # for item in target:
    #     if item == 1:
    #         count_1 += 1
    
    from heapq import heapify, heappop, heappush
    max_heap = [-item for item in target]
    heapify(max_heap)
    
    total_sum = -sum(max_heap)
    
    while True:
        largest = -heappop(max_heap)
        if largest == 1:
            return True
        
        total_sum -= largest
        if largest < total_sum:
            return False
        
        if total_sum == 1:
            return True
        elif total_sum < 1:
            return False
        
        # print('\n',largest, total_sum, max_heap)
        new_element = largest % total_sum
        total_sum = total_sum + new_element
        # print(largest, total_sum, new_element)
        # time.sleep(0.1)
        # if new_element
        
        if new_element < 1:
            return False
        heappush(max_heap, -new_element)
        
        


# target = [9,3,5]
# target =  [8,5]
# target = [1,9,1]
# target = [1, 100, 1]
# target = [1, int(1e9), 1, 4, 1]
target = [1, 2, 1, 1]
print(isPossible(target))
    
    