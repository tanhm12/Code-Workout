from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]):
        n = len(matrix)
        for m in range(n-n//2):
            for i in range(m, n-m-1): 
                cid = ((m,i), (i,n-m-1), (n-m-1, n-1-i), (n-1-i, m)) # clockwise id
                # print(m,i,cid)
                last = matrix[cid[-1][0]][cid[-1][1]]
                for j in range(3, 0, -1):
                    matrix[cid[j][0]][cid[j][1]] = matrix[cid[j-1][0]][cid[j-1][1]]
                
                matrix[cid[0][0]][cid[0][1]] = last
    

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)
for m in matrix:
    print(m)
                