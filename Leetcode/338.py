from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        sol = [0 for _ in range(n+1)]
        sol[1] = 1
        for i in range(1, n//2+1):
            left = 2*(i-1) + 2
            right = left + 1
            if left <= n:
                sol[left] = sol[i]
            if right <= n:
                sol[right] = sol[i] + 1
        
        return sol

print(Solution().countBits(1000))
            

        