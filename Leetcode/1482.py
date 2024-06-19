from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > len(bloomDay):
            return -1

        def is_valid(day: int) -> bool:
            target = m
            current_k = 0
            for i in range(n):
                if bloomDay[i] <= day:
                    current_k += 1
                    if current_k == k:
                        target -= 1
                        current_k = 0
                        if target == 0:
                            return True
                else:
                    current_k = 0
            if current_k == k:
                target -= 1
            return target <= 0


        l = 1
        r = max(bloomDay) + 1

        while l < r:
            day = (l+r) // 2
            # print(day, is_valid(day))
            if is_valid(day):
                r = day
            else:
                l = day + 1

        if is_valid(l):
            return l
        elif is_valid(l+1):
            return l + 1
        return -1


if __name__ == '__main__':
    bloomDay = [1,10,3,10,2]
    m=3
    k=1

    bloomDay = [7, 7, 7, 7, 12, 7, 7]
    m = 2
    k = 3
    print(Solution().minDays(bloomDay, m, k))
