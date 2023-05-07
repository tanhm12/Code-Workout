class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = int(1e9) + 7
        pows = [1 for i in range(len(nums) + 1)]  # precalculate sum of possible combinations of n distinct things; remmember The sum of all possible combinations of n distinct things is 2**n
        for i in range(1, len(pows)):
            pows[i] = (pows[i-1] * 2) % mod
        res = 0
        j = len(nums)-1

        for i in range(len(nums)):
            while j >= i and nums[i] + nums[j] > target:
                j -= 1
            if i > j:
                break
            res = (res + pows[j-i]) % mod  # remember The sum of all possible combinations of n distinct things is 2**n - 1

        return res            
