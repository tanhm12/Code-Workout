from typing import List

def maxAreaOfIsland(grid: List[List[int]]):
    m, n = len(grid), len(grid[0])
    # grid = [[0] * (n+2)] + grid + [[0] * (n+2)]
    # for j in 
    
    max_area = 0
    current_area = 0
    
    def find(i, j):
        nonlocal max_area, current_area
        if 0<=i<m and 0<=j<n:
            if grid[i][j] != 1:
                return
            if grid[i][j] == 1:
                current_area += 1
                max_area = max(current_area, max_area)
                grid[i][j] = -1
                # print(i,j, current_area)
                
                find(i-1, j)
                find(i+1, j)
                find(i, j-1)
                find(i, j+1)
                # current_area -= 1
                
        else:
            return
    
    for i in range(m):
        for j in range(n):
            current_area = 0
            find(i,j)
    
    return max_area

grid = [[0,0,0,0,0,0,0,0]]
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))   
    