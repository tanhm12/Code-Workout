from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [-1 for i in range(n+1)]
        
        
        def find_parent(u):
            if parent[u] < 0:
                return u
            parent[u] = find_parent(parent[u])
            return parent[u]
        
        def union(u, v):
            u1 = find_parent(u)
            v1 = find_parent(v)
            if u1 == v1:
                return False
            else:
                if parent[u1] > parent[v1]:
                    u1, v1 = v1, u1
                parent[u1] += parent[v1]
                parent[v1] = u1
                return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
                