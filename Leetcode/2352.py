from typing import List   
import hashlib 
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hashf = lambda x: hashlib.md5(";".join(x).encode()).hexdigest()
        hash_rows = defaultdict(int)
        hash_cols = defaultdict(int)
        for i in range(n):
            hash_rows[hashf(list(map(str, grid[i])))] += 1
            hash_cols[hashf(list(map(str, [grid[j][i] for j in range(n)])))] += 1
        
        res = 0
        for val in hash_rows:
            if val in hash_cols:
                res += hash_cols[val] * hash_rows[val]
        
        return res