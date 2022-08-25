
from typing import List
from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int):
        n += 1
        tcounter = Counter(tasks)
        
        
        if n < len(tcounter):
            res = 0
            tasks = [-tcounter[k] for k in tcounter]
            heapify(tasks)
            while True:
                exe_tasks = []
                tasks_len = len(tasks)
                for i in range(min(n, tasks_len)):
                    exe_tasks.append(heappop(tasks) + 1)
                for i in exe_tasks:
                    if i < 0:
                        heappush(tasks, i)
                res += n
                if len(tasks) <= n and min(tasks) == -1:
                    break
            
            return res + len(tasks)
        else:
            count = 0
            max_unique_task = 0
            for k in tcounter:
                if tcounter[k] > max_unique_task:
                    max_unique_task = tcounter[k]
            
            for k in tcounter:
                if tcounter[k] == max_unique_task:
                    count += 1
            return n * (max_unique_task-1) + count
    
tasks = ["A","A","A","B","B","B"]
n = 2

# tasks = ["A","A","A","B","B","B"]
# n = 0

# tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
# n = 2

print(Solution().leastInterval(tasks, n))
        
            