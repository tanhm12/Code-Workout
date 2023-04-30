from typing import List

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [-1 for i in range(n)]
    
    def find_parent(self, u):
        if self.parent[u] < 0:
            return u
        self.parent[u] = self.find_parent(self.parent[u])
        
        return self.parent[u]
    
    def union(self, u, v):
        u -= 1
        v -= 1
        pu = self.find_parent(u)
        pv = self.find_parent(v)
        if pu != pv:
            if pu > pv:
                pu, pv = pv, pu
            self.parent[pu] += self.parent[pv]
            self.parent[pv] = pu
            return True
        return False 
        

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a = UnionFind(n)
        b = UnionFind(n)
        counta = 0
        countb = 0
        edges_needed = 0
        for tp, u, v in edges:
            if tp == 3:
                ia = a.union(u, v) 
                ib = b.union(u, v)
                if ia or ib:
                    edges_needed += 1
                if ia:
                    counta += 1
                if ib:
                    countb += 1
                if counta >= n-1 and countb >= n-1:
                    break
                        
        
        for tp, u, v in edges:
            if tp == 1 and a.union(u, v):
                edges_needed += 1
                counta += 1
            elif tp == 2 and b.union(u, v):
                edges_needed += 1
                countb += 1
            if counta  >= n-1 and countb >= n-1:
                break  
        if counta < n-1 or countb < n - 1:
            return -1
        else:
            return len(edges) - edges_needed
        
        
                
        