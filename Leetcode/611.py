from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return  0
        nums.sort()
        res = 0
        for i1 in range(len(nums)-2):
            n1 = nums[i1]
            i3 = i1 + 1
            for i2 in range(i1+1, len(nums)-1):
                n2 = nums[i2]
                upper_bound = n1 + n2
                while i3 < len(nums) and nums[i3] < upper_bound:
                    i3 += 1
                if i3 == i2:
                    break
                res += i3 - i2 - 1
                # print(i1,i2,i3)
                if i3 == len(nums):
                    remain_pairs = i3-i2-2
                    res += remain_pairs*(remain_pairs+1)//2
                    break
        
        return res
    
nums = [2,2,3, 4]
# nums = [4,2,3,4]
nums = [1,2,3,4,5,6,7]
nums = [0,0,0]
print(Solution().triangleNumber(nums))
                    