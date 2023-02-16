from typing import List

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [-1 for i in range(len(s))]
        
        def find_parent(u):
            if parent[u] < 0:
                return u
            parent[u] = find_parent(parent[u])
            return parent[u]
        
        def union(u, v):
            pu = find_parent(u)
            pv = find_parent(v)
            if pu != pv:
                if pu > pv:
                    pu, pv = pv, pu
                parent[pu] += parent[pv]
                parent[pv] = pu
                
        for p1, p2 in pairs:
            union(p1, p2)
        
        groups = {}
        for i in range(len(s)):
            p = find_parent(i)
            if p not in groups:
                groups[p] = []
            groups[p].append(i)
        
        res = list(s)
        for k in groups:
            group_ids = sorted(groups[k])
            group_chars = sorted([s[i] for i in group_ids])
            # print(k, group_ids, group_chars)
            for i in range(len(group_ids)):
                res[group_ids[i]] = group_chars[i]
        
        return "".join(res)
        
        
        