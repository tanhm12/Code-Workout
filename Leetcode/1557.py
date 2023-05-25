
from typing import  List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        ein = defaultdict(int)
        for u, v in edges:
            ein[v] += 1
        
        return [u for u in range(n) if ein[u] == 0]