from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        def idx_to_cell_value(idx):
            r = idx // n
            c = max(0, idx - r * n)
            return matrix[r][c]
        
        lo = 0
        r = m * n - 1
        value = -1
        while lo < r:
            mid = (lo+r) // 2
            value = idx_to_cell_value(mid)
            if value == target:
                return True
            elif value > target:
                r = mid
            else:
                lo = mid + 1
        if lo == r and idx_to_cell_value(lo) == target:
            return True
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 10

print(Solution().searchMatrix(matrix, target))   