from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # check = lambda i, j:  0<=i<n and 0<=j<n
        res = 100 *n *n
        for i in range(1, n):
            for j in range(n):
                prev_ids = ((i-1, j))
                if j > 0:
                    prev_ids.append((i-1, j-1))
                if j < n-1:
                    prev_ids.append((i-1, j+1))
                matrix[i][j] += min([matrix[p0][p1] for p0, p1 in prev_ids])
                res = min(matrix[i][j], res)
        return res   
