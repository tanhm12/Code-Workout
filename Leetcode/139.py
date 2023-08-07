from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        mx_len = max([len(x) for x in wordDict])
        wordDict = set(wordDict)
        dp[0] = True
        for i in range(len(s)):
            if not dp[i]:
                continue
            for j in range(1, mx_len+1):
                idx = i+j
                if idx <= len(s):
                    if dp[idx]:
                        continue
                    elif s[i:i+j] in wordDict:
                        dp[idx] = True
                else:
                    break
        
        return dp[-1]
                
                