from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [0 for i in range(n)]
        res[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    res[j] = 0
                elif j > 0:
                    res[j] += res[j-1]
        
        return res[n-1]
