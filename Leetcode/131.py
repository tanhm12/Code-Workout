from typing import List
from functools import cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check_palindrome(start, end):
            end -= 1
            if start == end:
                return True
            mid =  (start + end-1) // 2 + 1
            # print(start, mid, end)
            for i in range(0, mid - start):
                if s[start + i] != s[end - i]:
                    return False
            return True
        
        @cache
        def find(pos):
            res = []
            for i in range(pos+1, len(s)+1):
                if check_palindrome(pos, i):
                    # print(pos, i)
                    res.extend([[s[pos:i]] + item for item in find(i)])
            if len(res) == 0:
                res = [[]]
            # print(pos, res)
            return res
        
        return find(0)

s = "aab"
# s = "aabnsdbfkdnfkdab"
s = "cdd"
print(Solution().partition(s))
        