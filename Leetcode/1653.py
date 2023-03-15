class Solution:
    def minimumDeletions(self, s: str) -> int:
        ca = s.count("a")
        res = ca
        cb = 0
        for c in s:
            if c == "b":
                cb += 1
            else:
                ca -= 1
            res = min(res, ca + cb)

        return res
        
        