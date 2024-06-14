from typing import List
from collections import Counter


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums_cnt = Counter(nums)
        sorted_keys = sorted(list(nums_cnt.keys()))
        cnt = sorted_keys[0]
        while cnt in nums_cnt:
            cnt += 1

        res = 0
        for num in sorted_keys:
            if nums_cnt[num] > 1:
                for i in range(nums_cnt[num]-1):
                    cnt = max(num+1, cnt)
                    while cnt in nums_cnt:
                        cnt += 1
                    res += cnt - num
                    cnt += 1

        return res