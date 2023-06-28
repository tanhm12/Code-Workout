class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1:
            return False
        dp = [False for _ in range(n+1)]
        dp[2] = True
        for i in range(3, n+1):
            for j in range(1, i):
                if i % j==0:
                    dp[i] = not dp[i-j]
                    if dp[i]:
                        break
        return dp[n]