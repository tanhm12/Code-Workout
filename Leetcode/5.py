class Solution:
    def longestPalindrome(self, s: str) -> str:
        idx = 0
        max_len = 0
        def findPalindrome(l, r):
            nonlocal idx, max_len
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            length = max(0, r-l-2)
            if length > max_len:
                max_len = length
                idx = l + 1
        
        for i in range(len(s)):
            findPalindrome(i, i+1)
            findPalindrome(i-1, i+1)
                

        return s[idx: idx + max_len + 1]

s = "bb"
s = "cbbd"
s = "abcda"
s = "afadsfkjfjkadsfe"
print(Solution().longestPalindrome(s))
