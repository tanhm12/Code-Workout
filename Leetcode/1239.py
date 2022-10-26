from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        darr = {}
        for s in arr:
            set_s = set(s)
            if len(set_s) == len(s):
                darr[s] = set_s
        arr = list(darr.keys())
        
        def check_intersection(s1, s2):
            if len(s2) > len(s1):
                s1, s2 = s2, s1
            for item in s2:
                if item in s1:
                    return True
            
            return False

        # candidates = {}
        # for i in range(len(arr)-1):
        #     candidates[arr[i]] = 0
        #     for j in range(i, len(arr)):
        #         if not check_intersection(darr[arr[i]], darr[arr[j]]) == 0:
        #             candidates[arr[i]].append(arr[j])
        
        def find(start, s: set):
            res = len(s)
            if start >= len(darr):
                return res
            
            for i in range(start, len(arr)):
                if not check_intersection(s, darr[arr[i]]):
                    res = max(res, find(i + 1, s.union(darr[arr[i]])))
            
            return res
        
        return find(0, set())


arr = ["un","iq","ue"]
arr = ["cha","r","act","ers"]
arr = ["abcdefghijklmnopqrstuvwxyz"]
print(Solution().maxLength(arr))
        