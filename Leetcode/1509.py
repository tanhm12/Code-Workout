from typing import List

class Solution:
    ## Short solution
    # def minDifference(self, nums: List[int]) -> int:
    #     if len(nums) <=4:
    #         return 0
    #     nums.sort()
    #     return min(
    #         abs(nums[-1]-nums[3]),
    #         abs(nums[-2]-nums[2]),
    #         abs(nums[-3]-nums[1]),
    #         abs(nums[0]-nums[-4]),
    #     )

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        from heapq import heapify, heappop
        heapify(nums)
        smallest = [heappop(nums) for _ in range(4)]
        nums.extend(smallest)

        nums = [-i for i in nums]
        heapify(nums)
        largest = [-heappop(nums) for _ in range(4)][::-1]

        return min(
            abs(largest[-1] - smallest[3]),
            abs(largest[-2] - smallest[2]),
            abs(largest[-3] - smallest[1]),
            abs(smallest[0] - largest[-4]),
        )
