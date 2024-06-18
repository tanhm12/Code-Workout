from typing import List
import bisect


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(profit, difficulty), key=lambda x: (x[0], -x[1]), reverse=True)
        worker.sort()
        print(worker)
        hi = len(worker)
        total_profit = 0
        for p, d in jobs:
            pos = bisect.bisect_left(worker, d, hi=hi)
            # print(p, d, pos, hi)
            if pos == hi or worker[pos] < d:
                continue
            else:
                total_profit += p * (hi-pos)
                hi = pos
                if hi == 0:
                    break
        return total_profit


if __name__ == '__main__':
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4,5,6,7]
    print(Solution().maxProfitAssignment(difficulty, profit, worker))