from typing import List


def searchMatrix(matrix: List[List[int]], target: int):
    m, n = len(matrix), len(matrix[0])
    
    def find(i, j):
        if 0<=i<m and 0<=j<n:
            # print(matrix[i][j])
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                return find(i+1, j)
            else:
                return find(i, j-1)
        else:
            return False
    
    return find(0, n-1)


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20

print(searchMatrix(matrix, target))