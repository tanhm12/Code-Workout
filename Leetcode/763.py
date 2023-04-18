class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        from collections import defaultdict
        mark = {s[i]: i for i in range(len(s))}
        res = []
        first = 0
        last = mark[s[0]]
        for i in range(len(s)):
            last = max(mark[s[i]], last)
            if i == last:
                res.append(last - first + 1)
                last = i + 1
                first = last
        return res

