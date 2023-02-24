class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for r in range(query_row):
            next_row = [0 for _ in range(r+2)]
            for c in range(r, -1, -1):
                row[c] -= 1
                if row[c] > 0:
                    next_row[c+1] += row[c] / 2
                    next_row[c] = row[c] / 2
            row = next_row
        return min(row[query_glass], 1)
    
print(Solution().champagneTower(1,1,1))
        