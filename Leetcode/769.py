from typing import List

def maxChunksToSorted(arr: List[int]):
    # arr = [[arr[i], i] for i in range(len(arr))]
    
    sorted_arr = sorted(arr)
    sorted_pos = {sorted_arr[i]: i for i in range(len(sorted_arr))}
    
    chunk = [0,0]
    count = 0
    for i in range(len(arr)):
        if sorted_pos[arr[i]] > chunk[1]:
            chunk[1] = sorted_pos[arr[i]]
        elif i == chunk[1]:
            count += 1
            chunk = [i+1, i+1]
    
    return count

arr = [1,0,2,3,4]
arr = [4,3,2,1,0]
arr = list(map(int, "2 1 3 0 4".split()))
arr = list(map(int, "1 2 3 5 0".split()))
print(maxChunksToSorted(arr))
    
    
    