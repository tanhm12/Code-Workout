from typing import List
    
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        size = 2*k + 1
        if size > n:
            return res
        
        cur_sum = 0
        for i in range(size):
            cur_sum += nums[i]
        
        nums.append(-1)
        for i in range(k, n - k):
            res[i] = cur_sum // size
            cur_sum = cur_sum - nums[i-k] + nums[i+k+1]
        
        return res
        
nums = [7,4,3,9,1,8,5,2,6] 
print(Solution().getAverages(nums, 3))