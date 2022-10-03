from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]):
        res = 0
        cur_time = neededTime[0]
        cur_max = neededTime[0]
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                cur_time += neededTime[i]
                cur_max = max(cur_max, neededTime[i])
            else:
                res += cur_time - cur_max
                cur_time = neededTime[i]
                cur_max = neededTime[i]
        res += cur_time - cur_max
        return res
    
print(Solution().minCost(colors = "abaac", neededTime = [1,2,3,4,5]))

print(Solution().minCost(colors = "abc", neededTime = [1,2,3]))
print(Solution().minCost(colors = "aabaa", neededTime = [1,2,3,4,1]))
print(Solution().minCost(colors = "aa", neededTime = [1, 2]))
        