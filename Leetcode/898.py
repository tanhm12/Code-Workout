from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        added = set()
        prev = set()
        for i in range(len(arr)):
            cand = arr[i]
            cur_set = set()
            cur_set.add(cand)
            
            for num in prev:
                cur_set.add(cand|num)

            added.update(cur_set)
            prev = cur_set
        return len(added)
            

if __name__ == "__main__":
    nums = [15,54,12,68,33,127,82,115,14]
    print(Solution().subarrayBitwiseORs(nums))