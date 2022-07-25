from typing import List

# def countSmaller(nums: List[int]):
#     from sortedcontainers import SortedList
#     sl = SortedList()
    
#     res = []
#     for i in range(len(nums) - 1, -1, -1):
#         res.append(sl.bisect_left(nums[i]))
#         sl.add(nums[i])
    
#     res.reverse()
#     return res


def countSmaller(nums: List[int]):
    res = [0 for _ in range(len(nums))]
    def mergeSort(arr):
        nonlocal res
        if len(arr) > 1:

            # Finding the mid of the array
            mid = len(arr)//2
    
            # Dividing the array elements
            L = arr[:mid]
    
            # into 2 halves
            R = arr[mid:]
    
            # Sorting the first half
            mergeSort(L)
    
            # Sorting the second half
            mergeSort(R)
    
            i = j = k = 0
    
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i][0] <= R[j][0]:
                    arr[k] = L[i]
                    i += 1
                    res[arr[k][1]] += j
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
    
            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                res[arr[k][1]] += j
                i += 1
                k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
                
                
    nums = [(nums[i],  i) for i in range(len(nums))]
    mergeSort(nums)
    return res


nums = [5,2,6,1]
# nums = [-1]
# nums = [-1,-1]

print(countSmaller(nums))
        
    
    