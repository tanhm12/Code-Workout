from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        largest = 1
        prev = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                if prev == -1:
                    largest = i
                    prev = i
                else:
                    largest = max(largest, (i - prev) // 2)
                    prev = i
        for i in range(len(seats)-1, -1, -1):
            if seats[i] == 1:
                return max(largest, len(seats) - i-1)
            
seats = [1,0,0,0]
# seats = [1,0,0,0,1,0,1]
seats = [1,0,0,1]
print(Solution().maxDistToClosest(seats))
                