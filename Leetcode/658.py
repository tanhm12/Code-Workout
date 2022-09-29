from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int):
        import bisect
        from collections  import deque
        pos = bisect.bisect_left(arr, x)
        if pos == 0 and arr[pos] > x:
            return arr[:k]
        if pos == len(arr):
            return arr[-k:]
        res = deque(maxlen=k)
        
        l = pos
        r = pos + 1
        
        if arr[pos] != x and arr[pos] - x >= x - arr[pos-1]:
            l = pos - 1
            r = pos
        print(l, r, pos)    
            
        while l >= 0 and r < len(arr) and len(res) < k:
            if x - arr[l] <= arr[r] - x:
                res.appendleft(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
       
        if len(res) < k:
            if l < 0:
                for i in range(k-len(res)):
                    res.append(arr[r+i])
            else:
                for i in range(k-len(res)):
                    res.appendleft(arr[l-i])
        
        return list(res)
    
    
# print(Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))
# print(Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3.5))
# print(Solution().findClosestElements(arr = [-2,-1,1,2,3,4,5], k = 7, x = 3))  
# print(Solution().findClosestElements(arr = [0,0,1,2,3,3,4,7,7,8], k = 3, x = 5))

print(Solution().findClosestElements(arr = [1,3], k = 1, x = 2))  