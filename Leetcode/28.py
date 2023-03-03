class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        elif needle == haystack[:len(needle)]:
            return 0
                    
        lps = [0] * len(needle)
        i = 1
        j = 0
        while i < len(needle):
            if needle[i] == needle[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j == 0:
                    lps[i] = 0
                    i += 1
                else:
                    j = lps[j-1]
          
        i = 0
        j = 0
        while i < len(haystack):
            while i < len(haystack) and haystack[i] == needle[j] :
                i += 1
                j += 1
                if j == len(needle):
                    return i-j
            
            if i >= len(haystack):
                return -1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
        
        return -1
            
        