
from typing import List

def makesquare(matchsticks: List[int]):
    if len(matchsticks) < 4:
        return False
    
    from collections import defaultdict
    freq = defaultdict(int)
    s = 0
    
    for i in matchsticks:
        s += i
        freq[i] += 1
    
    freq = dict(freq)
    if s % 4 != 0:
        return False
    
    target = s // 4
    # print(s, target)
    

    res = False
    matchsticks.sort(reverse=True)
    
    parts = [0 for _ in range(4)]
    
    def find(pos):
        nonlocal res
        for i in range(4):
            if parts[i] > target:
                return False
        if pos == len(matchsticks):
            # print(parts)
            if parts[0]==parts[1]==parts[2]==parts[3]:
                res = True
                return True
            else:
                return False
        else:
            for i  in range(4):
                if parts[i] + matchsticks[pos] <= target:
                    parts[i] += matchsticks[pos]
                    if find(pos + 1):
                        return True
                    parts[i] -= matchsticks[pos]
                    if parts[i] == 0:
                        break
    
    find(0)
    
    return res
    

matchsticks = [1,1,2,2,2]
matchsticks = [3,3,3,3,4]
matchsticks = [3,1,2, 2, 1, 1, 1, 1]
# matchsticks = [2, 2, 2]
# matchsticks = [8,2 ,1 ,1]
matchsticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# matchsticks = [3,3,2,2,2,2,2,2,2,2,2,2,2,2,2]
matchsticks =  [14,10,10,10,10,10,10,10,10,10,10,10,8,9,19]
print(makesquare(matchsticks))
    
    