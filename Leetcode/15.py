from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        import bisect
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            remain = 0 - nums[i]
            fp = i + 1
            sp = len(nums)

            while fp < sp:
                tgt = remain - nums[fp]
                sp = bisect.bisect_left(nums, tgt, lo=fp+1, hi=sp)
                if sp < len(nums) and nums[sp] == tgt:
                    res.append([nums[i], nums[fp], nums[sp]])
                fp = bisect.bisect(nums, nums[fp], lo=fp)
                
        return res


nums = [0,0,0]
# nums = [-1,0,1,2,-1,-4]
# nums = [0, 1, 1]
# nums = [0,0,0,0]
# nums = [0] * 3000
# nums = [1,-1,-1,0]
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

print(Solution().threeSum(nums))
# print(nums)

    