from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roads = [[i-1, j-1, k] for i, j, k in roads]
        parent = [-1 for i in range(n)]
        score = [1e5 for i in range(n)]

        def find_parent(u):
            if parent[u] < 0:
                return u
            
            parent[u] = find_parent(parent[u])
            return parent[u]

        def merge(u, v, dis):
            pu = find_parent(u)
            pv = find_parent(v)
            
            if pu != pv:
                if parent[pu] > parent[pv]:
                    pu, pv = pv, pu
                parent[pu] += parent[pv]
                parent[pv] = pu
            score[pu] = min(score[pu], score[pv], dis)
        
        for u, v, dis in roads:
            merge(u, v, dis)
        
        return score[find_parent(0)]

        