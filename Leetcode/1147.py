from functools import cache

class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        mid = n // 2 +1
        def solve(i):
            end = n - i
            res = 1
            print(i, end, mid)
            if i >= end:
                return 0
            for j in range(i+1, mid):
                # print(i, j, end, text[i:j], text[end-j+i:end])
                if text[i:j] == text[end-j+i:end]:
                    return solve(j) + 2
            return res
        return solve(0)
    
text = "ghiabcdefhelloadamhelloabcdefghi"
text = "antaprezatepzapreanta"
text = "antaprezatepzapreanta" * 47
# text = "antaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreantaantaprezatepzapreanta"
text = "aaa"

print(len(text), text)
print(Solution().longestDecomposition(text))
            
        