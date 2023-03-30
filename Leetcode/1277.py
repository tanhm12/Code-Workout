from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ## number of squares that have (i, j) as bottom right corner is also the edge size of largest square with(i, j) as bottom right corner
        ## dp[i][j] is the size of largest square with(i, j) as bottom right corner
        ## --> dp[i][i] can be expanded from its left, above and left diagonal cells --> min size of 3 squares 
        res = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] and i > 0 and j > 0:
                    matrix[i][j] =  min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1
                res += matrix[i][j]
        return res 
        
        