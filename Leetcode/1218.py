from typing import List
import bisect

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = 0
        dp = {}
        
        for i, num in enumerate(arr):
            prev = num - difference
            if prev in dp:
                dp[num] = dp[prev] + 1
            else:
                dp[num] = 1
            res = max(res, dp[num])
        
        return res