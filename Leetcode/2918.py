from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        def get_stats(nums):
            sums = 0
            cnt = 0
            for i in nums:
                sums += i
                if i == 0:
                    cnt += 1
            
            return sums, cnt
        
        sums1, cnt1 = get_stats(nums1)
        sums2, cnt2 = get_stats(nums2)
        # print(sums1, sums2, cnt1, cnt2)
        
        if sums2 > sums1:
            sums1, sums2 = sums2, sums1
            cnt1, cnt2 = cnt2, cnt1
            
        if sums1 == sums2:
            if cnt1 == 0 or cnt2 == 0:
                if cnt1 == cnt2:
                    return sums1
                else:
                    return -1
            return sums1 + max(cnt1, cnt2)
        else:  # sums1 > sums2
            if cnt2 == 0 or (cnt1 == 0 and cnt2 > sums1 - sums2):
                return -1
            return max(sums1 + cnt1, sums2 + cnt2)
            
        
    
# import random   
# def random_array(size: int, val_range = (0, 10)):
#     res = [random.randint(*val_range) for _ in range(size)]
#     return res

# print(random_array(100))
# print(random_array(20))    

if __name__ == "__main__":
    
    nums1 = [3,2,0,1,0]
    nums2 = [6,5,0]
    # nums1 = [8,13,15,18,0,18,0,0,5,20,12,27,3,14,22,0]
    # nums2 = [29,1,6,0,10,24,27,17,14,13,2,19,2,11]

    print(Solution().minSum(nums1, nums2))
    