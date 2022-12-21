from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = [i ^ (i>>1) for i in range(2**n)]
        for i in range(len(res)):
            if res[i] == start:
                return res[i:] + res[:i]

n, start = 2, 3
n, start = 8, 0
print(Solution().circularPermutation(n ,start))