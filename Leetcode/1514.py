from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            adj[u].append((-succProb[i], v))
            adj[v].append((-succProb[i], u))
        
        if len(adj[start]) == 0:
            return 0
        
        from heapq import heappush,  heappop, heapify
        d = [2 for _ in range(n)]
        for prob, v in adj[start]:
            d[v] = prob
        check = [False for _ in range(n)]
        heap = adj[start][:]
        heapify(heap)
        while len(d) > 0:
            while len(heap) > 0 and check[heap[0][1]]:
                heappop(heap)
            if len(heap) == 0:
                return 0
            prob, u = heappop(heap)
            d[u] = -prob
            check[u] = True
            if u == end:
                return d[u]
            for next_prob, v in adj[u]:
                if not check[v]:
                    heappush(heap, (-prob * next_prob, v))
        
        return 0
                
        
        