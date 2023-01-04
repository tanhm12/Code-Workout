from typing import List

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        from collections import Counter
        c = Counter(tasks)
        res = 0
        for t in c:
            if c[t] == 1:
                return -1
            res += c[t] // 3
            if c[t] % 3 !=0:
                res += 1
        
        return res

