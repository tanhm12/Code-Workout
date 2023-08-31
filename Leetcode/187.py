from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import defaultdict
        if len(s) < 10:
            return []
        chars = "ATGC"
        charmap = {chars[i]: i for i in range(4)}
        cands = defaultdict(int)
        cur = 0
        for i in range(10):
            cur = (cur << 2) + charmap[s[i]]
        cands[cur] += 1
        
        mod_val = 4**9
        for i in range(10, len(s)):
            cur = cur % mod_val
            cur = (cur << 2) + charmap[s[i]]
            cands[cur] += 1
        

        res = [item for item in cands if cands[item] > 1]
        for i in range(len(res)):
            text = ""
            cur = res[i]
            for j in range(10):
                text += chars[cur%4]
                cur = cur >> 2
            res[i] = text[::-1]
        return res

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAAAA"
s = "GAGAGAGAGAGA"
print(Solution().findRepeatedDnaSequences(s))