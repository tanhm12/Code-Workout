from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for __ in range(n)]
        def gen(r, start):
            diff = n-2*r - 1
            last_row = n-r-1
            for i in range(r, n-r-1):
                res[r][i] = start
                res[i][last_row] = start + diff
                offset = n-i-1
                res[last_row][offset] = res[i][last_row] + diff
                res[offset][r] = res[last_row][offset] + diff
                start += 1
            return start + diff * 3
        
        start = 1
        for i in range(n//2):
            start = gen(i, start)
        
        if n % 2 != 0:
            mid = n//2 
            res[mid][mid] = n**2
        
        return res

n = 5
res = Solution().generateMatrix(n)
for i in res:
    print(i)
        