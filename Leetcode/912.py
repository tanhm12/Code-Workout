from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, left, right):
            if left >= right:
                return
            pivot_pos = random.randint(left, right)
            arr[pivot_pos], arr[left] = arr[left], arr[pivot_pos]
            pivot = arr[left]
            lp = left
            rp = right
            while lp < rp:
                while arr[lp] <= pivot and lp < right:
                    lp += 1
                while arr[rp] > pivot and rp > left:
                    rp -= 1
                if rp > lp:
                    arr[lp], arr[rp] = arr[rp], arr[lp]
            arr[rp], arr[left] = arr[left], arr[rp]
            lp = rp
            while lp > left and arr[lp] == pivot:
                lp -= 1
            while rp < right and arr[rp] == pivot:
                rp += 1
            return lp, rp

        def quick_sort(arr, left, right):
            if left >= right:
                return
            lp, rp = partition(arr, left, right)
            quick_sort(arr, left, lp)
            quick_sort(arr, rp, right)

        quick_sort(nums, 0, len(nums)-1)
        return nums

if __name__ == '__main__':
    nums = [5,1,1,2,0,0]
    nums = [2] * 50000
    # print(len(nums))
    # print(Solution().sortArray(nums))