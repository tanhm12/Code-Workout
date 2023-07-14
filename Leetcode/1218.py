from typing import List
import bisect

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        all_pos = {}
        for i, j in enumerate(arr):
            if j in all_pos:
                all_pos[j].append(i)
            else:
                all_pos[j] = [i]
        
        res = [1] * n
        for i, num in enumerate(arr):
            prev = num - difference
            if prev in all_pos:
                pos = bisect.bisect_left(all_pos[prev], i)
                if pos == 0:
                    continue
                pos -= 1
                res[i] = res[all_pos[prev][pos]] + 1
        
        return max(res)