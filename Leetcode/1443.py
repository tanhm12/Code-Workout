from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        neighbors = [[] for i in range(n)]
        
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
        
        check = [False for i in range(n)]
        
        def travel(v):
            check[v] = True
            total_time = sum([travel(u) for u in neighbors[v] if not check[u]])
            if total_time != 0 or hasApple[v]:
                total_time += 2
            return total_time

        return max(travel(0)-2, 0)
            

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]

n = 8
edges = [[0,1],[1,2],[2,3],[1,4],[2,5],[2,6],[4,7]]
hasApple = [True,True,False,True,False,True,True,False]

n = 4
edges = [[0,2],[0,3],[1,2]]
hasApple = [False, True, False, False]

print(Solution().minTime(n,edges, hasApple))