import math

class Solution:
    def numSquares(self, n: int) -> int:
        sqrts = []
        for i in range(1, round(math.sqrt(n)) + 1):
            sqrts.append(i**2)

        dp = [int(1e5) for i in range(n+1)]
        dp[0] = 0
        
        for i in range(1, n+1):
            for s in sqrts:
                if i < s:
                    break
                dp[i] = min(dp[i], dp[i-s] + 1)
                    
        return dp[n]


class Solution:
    _dp = [0]
    _sqrts = [1]
    def numSquares(self, n: int) -> int:
        dp = self._dp
        sqrts = self._sqrts
        if n < len(dp):
            return dp[n]
        
        start = int(sqrts[-1] ** 0.5) + 1
        if start ** 2 == sqrts[-1]:
            start += 1
        for i in range(start, round(n**0.5) + 1):
            sqrts.append(i**2)
        
        start = len(dp)
        for i in range(start, n+1):
            dp.append(int(1e5))
            for s in sqrts:
                if i < s:
                    break
                dp[i] = min(dp[i], dp[i-s] + 1)
        
        return dp[n]

while True:
    print(Solution().numSquares(int(input())))