from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        res = [0 for i in range(n)]
        for i in range(n):
            res[i] = max(res[i], res[i-1])
            p, b = questions[i]
            next_idx = i + b + 1
            if next_idx < n:
                res[next_idx] = max(res[next_idx], res[i] + p)
        for i in range(n):
            res[i] += questions[i][0]
        return max(res)

questions = [[3,2],[4,3],[4,4],[2,5]]
questions = [[12,46],[78,19],[63,15],[79,62],[13,10]]
# questions = [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]
print(Solution().mostPoints(questions))
        