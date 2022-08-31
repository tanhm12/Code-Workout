from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]):
        m, n = len(heights), len(heights[0])
        
        p_visited = set()
        a_visited = set()
        
        def travel(i, j, visited):
            if (i, j) in visited:
                return 
            visited.add((i, j))
            
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0<=ni<m and 0<=nj<n and heights[ni][nj] >= heights[i][j] :
                    travel(ni, nj, visited)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    travel(i, j, p_visited)
                if i == m-1 or j == n-1:
                    travel(i, j, a_visited)
        
        return list(p_visited & a_visited)
    
    
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# heights = [[1]]
# heights = [[10,10,10],[10,1,10],[10,10,10]]

print(Solution().pacificAtlantic(heights))
        
        