from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        from collections import defaultdict
        res = [defaultdict(int) for _ in range(n)]
        
        check = [False for i in range(n)]
        def dfs(u):
            check[u] = True
            res[u][labels[u]] += 1
            for v in adj[u]:
                if not check[v]:
                    dfs(v)
                    for c in res[v]:
                        res[u][c] += res[v][c]
        dfs(0)
        res = [res[u][labels[u]] for u in range(n)]
        return res