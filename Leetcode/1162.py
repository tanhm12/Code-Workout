from typing import List
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        from queue import Queue
        n = len(grid)
        
        def neighbors(u):
            x, y = u
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0<=i<n and 0<=j<n and grid[i][j] == 0:
                    yield (i,j)
                    
        all_land_cells = [(i, j) for i in range(n) for j in range(n) if grid[i][j]==1]
        
        q = Queue()
        for cell in all_land_cells:
            q.put((cell, 0))
        distance = 0
        
        while not q.empty():
            u, distance = q.get()
            
            for v in neighbors(u):
                grid[v[0]][v[1]] = 1
                q.put((v, distance+1))
        
        
        if distance == 0:
            return -1
        
        return distance
        