



def isInterleave(s1: str, s2: str, s3: str):
    if len(s1) + len(s2) != len(s3):
        return False
    from functools import lru_cache
    @lru_cache(40000)
    def check(i1, i2):
        i = i1 + i2
        if i >= len(s3) \
            or (i1 < len(s1) and s1[i1] == s3[i] and check(i1 + 1, i2)) \
            or (i2 < len(s2) and s2[i2] == s3[i] and check(i1, i2 + 1)):
            return True
        return False    
    
    return check(0, 0)

print(isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))
print(isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
print(isInterleave(s1 = "", s2 = "", s3 = ""))
    