from typing import List

def findJudge(n: int, trust: List[List[int]]):
    from collections import defaultdict
    
    count = defaultdict(int)
    reverse_count = set()
    for i, j in trust:
        count[j] += 1
        reverse_count.add(i)
    
    for j in count:
        if count[j] == n-1 and j not in reverse_count:
            return j
            
        
    return -1
    

n = 2
trust = [[1,2]]

n = 3
trust = [[1,3],[2,3]]

n = 3
trust = [[1,3],[2,3],[3,1]]

print(findJudge(n, trust))

