class Solution:
    str2int =  set([str(i) for i in range(1, 27)])
    
    def numDecodings(self, s: str) -> int:
        count = lambda x: 1 if x in Solution.str2int else 0
        dp = [1 for _ in range(len(s) + 1)]
        dp[1] = count(s[0])
        for i in range(1, len(s)):
            dp[i+1] = count(s[i]) * dp[i] + count(s[i-1:i+1]) * dp[i-1]
        return dp[len(s)]