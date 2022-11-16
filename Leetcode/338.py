from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        sol = [0 for _ in range(n+1)]
        sol[1] = 1
        for i in range(2, n+1):
            exact_idx = i - 1
            if exact_idx % 2 == 0:
                exact_idx -= 2
                parent_idx = exact_idx // 2 + 1
                sol[i] = sol[parent_idx] + 1
            else:
                exact_idx -= 1
                parent_idx = exact_idx // 2 + 1
                sol[i] = sol[parent_idx]
        
        return sol

print(Solution().countBits(1000))
            

        