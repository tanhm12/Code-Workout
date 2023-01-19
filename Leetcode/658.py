from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int):
        import bisect
        pos = bisect.bisect_left(arr, x)
        if pos == 0 and arr[pos] > x:
            return arr[:k]
        if pos == len(arr):
            return arr[-k:]
        
        l = pos
        r = pos + 1
        
        if arr[pos] != x and arr[pos] - x >= x - arr[pos-1]:
            l = pos - 1
            r = pos

        while l >= 0 and r < len(arr) and r-l <= k:
            if x - arr[l] <= arr[r] - x:
                l -= 1
            else:
                r += 1
                 
        l += 1        
        if l == 0:
            r += k - (r-l)
        else:
            l -= k - (r-l)      

        return arr[l:r]