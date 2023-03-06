from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n  = len(arr)
        if arr[0] > k:
            return k
        elif arr[-1] - n < k:
            return k + n
        l = 0
        r = n-1
        while l < r:
            m = (l + r) // 2
            if arr[m] - m - 1 < k:
                l = m+1
            else:
                r = m
        
        return l + k
    

arr = [1,2,3,4]
k = 2

arr = [2,3,4,7,11]
k = 5
print(Solution().findKthPositive(arr, k))
        
        