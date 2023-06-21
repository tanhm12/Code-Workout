class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import Counter
        counter_s = Counter(s)
        counter_t = Counter(t)

        if sorted(counter_s.values()) != sorted(counter_t.values()):
            return False

        def make_map(counter):
            count = 0
            res = {}
            counter = sorted(dict(counter), key=lambda x: counter[x])
            for c in counter:
                res[c] = count
                count += 1
            return res
        
        maps = make_map(counter_s)
        mapt = make_map(counter_t)
        
        for i in range(len(s)):
            if maps[s[i]] != mapt[t[i]]:
                return False
        return True