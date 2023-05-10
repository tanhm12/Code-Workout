class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [[0 if i !=j else 1 for i in range(len(s))] for j in range(len(s))]
        idx = (0, 0)
        cur_max = 0
        for i in range(len(s)-1, -1, -1):
            res[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j == i+1:
                        res[i][j] = 2
                    elif res[i+1][j-1] != 0:
                        res[i][j] = res[i+1][j-1] + 2
                    if res[i][j] > cur_max:
                        cur_max = res[i][j]
                        idx = (i, j)

        return s[idx[0]:idx[1]+1]
