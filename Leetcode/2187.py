from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 0
        r = min(time) * totalTrips + 1
        
        while l < r:
            min_time = (l+r) // 2
            cur = 0
            for t in time:
                cur += min_time // t 
            
            if cur < totalTrips:
                l = min_time + 1
            else:
                r = min_time 
        
        return l

time = [1,2,3]
totalTrips = 5

time = [2]
totalTrips = 2

print(Solution().minimumTime(time, totalTrips))

        