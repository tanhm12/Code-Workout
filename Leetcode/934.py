from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        from queue import Queue
        n = len(grid)
        q = Queue()  
        check = [[False for _ in range(n)] for __ in range(n)]
        
        def dfs(x, y):
            check[x][y] = True
            q.put((x, y, 0))
            for i, j in ((x, y+1), (x, y-1), (x-1, y), (x+1, y)):
                if 0<=i < n and 0<=j <n and grid[i][j]==1 and not check[i][j]:
                    dfs(i, j)
        
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break
                
        # print(check)
                    
        while not q.empty():
            x, y, dis = q.get()
            for i, j in ((x, y+1), (x, y-1), (x-1, y), (x+1, y)):
                if 0<=i < n and 0<=j <n and not check[i][j]:
                    check[i][j] = True
                    if grid[i][j] == 1:
                        return dis
                    q.put((i, j, dis + 1))

# grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
grid = [[0,1,0],[0,0,0],[0,0,1]]

print(Solution().shortestBridge(grid))
            
        