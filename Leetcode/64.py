from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = [[False for _ in range(n)] for __ in range(m)]
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0:
                    result[i][j] = min(result[i-1][j], result[i][j-1])
                elif j == 0:
                    result[i][j] = result[i-1][j]
                elif i == 0:
                    result[i][j] = result[i][j-1]
                result[i][j] += grid[i][j]
        
        return result[m-1][n-1]
        