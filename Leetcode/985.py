from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]):
        res = []
        s = sum([i for i in nums if i % 2 == 0])
        for val, i in queries:
            if nums[i] % 2 == 0:
                nums[i] += val
                if val % 2 == 0:
                    s += val
                else:
                    s -= nums[i] - val
            else:
                nums[i] += val
                if val % 2 == 1:
                    s += nums[i]
            res.append(s)
        
        return res

nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

nums = [1]
queries = [[4,0]]

print(Solution().sumEvenAfterQueries(nums, queries))
        