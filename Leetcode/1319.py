from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
            
        parent = [-1 for i in range(n)]

        def find_parent(u):
            if parent[u] < 0:
                return u
            
            parent[u] = find_parent(parent[u])
            return parent[u]

        def merge_network(u, v):
            pu = find_parent(u)
            pv = find_parent(v)
            
            if pu != pv:
                if parent[pu] > parent[pv]:
                    pu, pv = pv, pu
                parent[pu] += parent[pv]
                parent[pv] = pu
                
                return True
            return False
        
        num_of_edges = 0
        
        for u, v in connections:
            if merge_network(u, v):
                num_of_edges += 1
        
        return n - 1 - num_of_edges
            
        