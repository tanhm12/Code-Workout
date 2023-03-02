from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distances = []
        for i in range(0, len(points)-1):
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                distances.append((distance, i, j))
                distances.append((distance, j, i))
        
        from heapq import heapify, heappop
        heapify(distances)
        res = 0
        cluster =  [-1 for i in range(n)]
        def find_cluster(u):
            if cluster[u] < 0:
                return u
            cluster[u] = find_cluster(cluster[u])
            return cluster[u]

        
        def merge(distance, u, v):
            nonlocal res
            pu = find_cluster(u)
            pv = find_cluster(v)
            if pu == pv and cluster[pu] == -n:
                return True
            if pu != pv:
                res += distance
                if pu > pv:
                    pu, pv = pv, pu
                cluster[pu] += cluster[pv]
                cluster[pv] = pu
        
        while len(distances) > 0:
            distance, u, v = heappop(distances)
            if merge(distance, u, v):
                return res
        
        return 0
                
        
        