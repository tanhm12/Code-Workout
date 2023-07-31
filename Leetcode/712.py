class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        res = [[0] * (n2+1) for i in range(n1+1)]
        
        for i in range(n1+1):
            for j in range(n2+1):
                if i == 0 or j == 0:
                    continue
                elif s1[i-1] == s2[j-1]:
                    res[i][j] = max(res[i-1][j-1] + ord(s1[i-1]), res[i-1][j], res[i][j-1])
                else:
                    res[i][j] = max(res[i-1][j], res[i][j-1])
                    
        return sum(ord(c) for c in s1) + sum(ord(c) for c in s2) - 2*res[-1][-1]

s1 = "delete"
s2 = "leet"

print(Solution().minimumDeleteSum(s1, s2))

