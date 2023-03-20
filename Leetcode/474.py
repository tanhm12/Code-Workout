from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs = [(x, x.count("0"), len(x) - x.count("0")) for x in strs]
        strs = [item for item in strs if item[1] <= m and item [2] <= n]
        res = [[0] * (n+1) for i in range(m+1)]
        
        # for i in range(m+1):
        #     res[i][0] = 0
        # for j in range(n+1):
        #     res[0][j] = 0
           
        
        for _, zeros, ones in strs:
            for i in range(m, zeros-1, -1):
                i_zero = i - zeros
                for j in range(n, ones-1, -1):
                    j_one = j - ones
                    res[i][j] = max(res[i][j], res[i_zero][j_one] + 1)
        
        return res[-1][-1]
        
        
        