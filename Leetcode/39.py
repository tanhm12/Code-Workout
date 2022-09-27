from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int):
        candidates.sort()
        
        def find(remain, pos):
            if remain == 0:
                return [[]]
            cands = []
            for i in range(pos, len(candidates)):
                c = candidates[i]
                if c <= remain:
                    cands.extend([[c] + arr for arr in find(remain-c, i)])
            # print(remain, cands)
            return cands
        return find(target, 0)
    
    
candidates = [2,3,6,7, 1, 4, 5]
target = 7 * 2
print(Solution().combinationSum(candidates, target))

        