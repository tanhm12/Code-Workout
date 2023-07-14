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
        cur_pos = {i: 0 for i in all_pos}
        for i, num in enumerate(arr):
            prev = num - difference
            if prev in all_pos:
                while cur_pos[prev] < len(all_pos[prev]) and all_pos[prev][cur_pos[prev]] < i:
                    cur_pos[prev] += 1
                if cur_pos[prev] == 0:
                    continue
    
                res[i] = res[all_pos[prev][cur_pos[prev]-1]] + 1
        
        return max(res)