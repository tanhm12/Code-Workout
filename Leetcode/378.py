from typing import List

def kthSmallest(matrix: List[List[int]], k: int):
    for i in matrix:
        print(i)
        
        
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print(kthSmallest(matrix, k))
    