from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        accumulation = [0] * (n + 1)
        for i in range(n):
            accumulation[i + 1] = -customers[i] * (grumpy[i]-1) + accumulation[i]
        res = 0
        for i in range(minutes):
            res += customers[i]
        sliding = res
        res += accumulation[-1] - accumulation[minutes]
        # print(res, sliding, accumulation)

        for i in range(minutes, n):
            sliding = sliding - (customers[i - minutes]) + \
                      customers[i]
            # print(i, sliding, accumulation[i-minutes+1], accumulation[-1]-accumulation[i+1])
            res = max(res, accumulation[i-minutes+1] + sliding + accumulation[-1]-accumulation[i+1])

        return res


if __name__ == '__main__':
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy =    [0, 1, 0, 1, 0, 1, 0, 1]
    minutes = 3

    print(Solution().maxSatisfied(customers, grumpy, minutes))