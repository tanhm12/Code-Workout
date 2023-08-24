from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        
        def is_possible(distance):
            cur = 0
            remain = m - 1
            for i in range(1, n):
                if position[i] - position[cur] >= distance:
                    # print(i, cur, remain)
                    cur = i
                    remain -= 1
                    if remain <= 0:
                        break
            return remain <= 0

        l = 1
        r = position[-1] - position[0]
        while l < r:
            mid = (l+r) // 2
            # print(mid, is_possible(mid))
            if is_possible(mid):
                l = mid + 1
            else:
                r = mid
        
        return l if is_possible(l) else l-1

position = [5,4,3,2,1,1000000000]
m = 2

position = [1,2,3,4,7]
m = 3
print(Solution().maxDistance(position, m))
  
        