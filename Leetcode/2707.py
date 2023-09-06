from typing import List
from functools import cache

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        @cache
        def find_optimal(pos):
            if pos == len(s):
                return 0
            res_pos = len(s) - pos
            for i in range(pos + 1, len(s) + 1):
                cur_res = find_optimal(i)
                if s[pos:i] not in dictionary:
                    cur_res += i - pos
                res_pos = min(res_pos, cur_res)
            
            return res_pos
        
        return find_optimal(0)
                
s = "leetscode"
dictionary = ["leet","code","leetcode"]   

s = "sayhelloworld"
dictionary = ["hello","world"]

s = "sayhelloworldleetscodesayhelloworldleetscodeldleet"
dictionary = ["leet","code","leetcode", "hello","world"]   
print(len(s))
print(Solution().minExtraChar(s, dictionary))     