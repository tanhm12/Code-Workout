from heapq import heappush, heappushpop,  heapify
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if len(nums) > k:
            self.q = sorted(nums)[len(nums)-k:]
        else:
            self.q =  nums
        heapify(self.q)

    def add(self, val: int) -> int:
        if len(self.q) < self.k:
            heappush(self.q, val)
        elif val >= self.q[0]:
            heappushpop(self.q, val)
        return self.q[0]
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)