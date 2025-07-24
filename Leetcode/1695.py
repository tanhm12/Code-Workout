from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = nums[0]
        cur_range = [0, 0]
        cur_sum = nums[0]
        S = {nums[0]: 0}
        for i in range(1, len(nums)):
            cur_sum += nums[i]
            if nums[i] in S:
                start, end = cur_range
                del_end = S[nums[i]]
                for j in range(start, del_end+1):
                    cur_sum -= nums[j]
                    del S[nums[j]]
                cur_range = [del_end+1, i]
                
            else:
                cur_range[1] += 1
            S[nums[i]] = i
            # print(i, nums[i], S)
            if cur_sum > res:
                res = cur_sum
        
        return res
    
if __name__ == "__main__":
    nums = [5,2,1,2,5,2,1,2,5]
    print(Solution().maximumUniqueSubarray(nums))
                    