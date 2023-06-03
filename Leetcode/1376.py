from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children_of = [[] for _ in range(n)]
        for i, e in enumerate(manager):
            if e != -1:
                children_of[e].append(i)
        
        def solve(i) -> int:
            if len(children_of[i]) == 0:
                return 0
            return max(solve(j) for j in children_of[i]) + informTime[i]
        
        return solve(headID)
        