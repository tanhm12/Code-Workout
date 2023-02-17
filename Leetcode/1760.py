from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 0
        r = 10**9
        while l < r:
            mid = (l+r) // 2  # penalty, max size of a bag after operations
            if mid == 0:
                break
            op_count = 0
            for i in nums:  # check if possible to get mid penalty after maxOperations
                if i > mid:
                    op_count += i // mid
                    if i % mid == 0:
                        op_count -= 1
                    if op_count > maxOperations:
                        break
            if op_count > maxOperations: 
                l = mid+1
            else:
                r = mid
            
        return r
        
        