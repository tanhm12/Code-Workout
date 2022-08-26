from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int):
        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        check = [False for i in range(n)]
        
        def travel(src):
            if src == destination:
                return True
            res = False
            check[src] = True
            for v in adj[src]:
                if not check[v]:
                    res = res or travel(v)
            
            return res
        
        return travel(source)
    
    
    def validPathDisjoint(self, n: int, edges: List[List[int]], source: int, destination: int):
        pass
        

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

print(Solution().validPath(n, edges, source, destination))
        