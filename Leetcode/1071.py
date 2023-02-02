class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        
        if len(set(s1)) == 1:
            return s1
        elif s1[0] != s2[0]:
            return ""
        mark = 0
        i = 1
        while i <= len(s1)//2:
            if s1[i] == s1[0]:
                equal = True
                for j in range(i):
                    if s1[j] != s1[i+j]:
                        equal = False
                        break
                if equal:
                    mark = max(mark, i)
            i += 1
        return s1[:mark] if mark > 0 else s1
