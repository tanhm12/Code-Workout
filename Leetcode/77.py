from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        check = [False for _ in range(n+1)]
        sol = [0] * k
        def gen(i, j):
            if j == k:
                res.append(sol[:])
                return
            if i > n:
                return
            for ni in range(i, n + 2 + j - k):
                if not check[ni]:
                    check[ni] = True
                    sol[j] = ni
                    gen(ni+1, j+1)
                    check[ni] = False
            
        gen(1, 0)
        return res 

print(Solution().combine(10, 2))
                    