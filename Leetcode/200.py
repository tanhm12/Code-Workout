from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]):
        n, m = len(grid), len(grid[0])
        def travel(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= ni < n and 0 <= nj < m:
                        travel(ni, nj)
        
        num_island = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    num_island += 1
                    travel(i, j, num_island+1)
        
        return num_island
    
    
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(Solution().numIslands(grid))
        