from typing import List
from collections import Counter, deque

class Solution:
    def findOriginalArray(self, changed: List[int]):
        counter = Counter(changed)
        res = []
        if 0 in counter:
            if counter[0] % 2 != 0:
                return []
            else:
                res.append([0] * (counter[0] // 2))
                del counter[0]
                
        res = []
        keys = list(counter.keys())
        
        for k in keys:
            if k not in counter:
                continue
            
            sequence = deque([k])
            left = k 
            
            while True:
                if left % 2 != 0:
                    break
                else:
                    left = left // 2
                    if left not in counter or left == 0:
                        break
                    sequence.appendleft(left)
            
            right = k * 2
            while right in counter:
                sequence.append(right)
                right *= 2
            
            sequence = list(sequence)
            if len(sequence) == 1:
                return []
            # print(sequence)
            for i in range(len(sequence) - 1):
                if counter[sequence[i]] == 0:
                    del counter[sequence[i]]
                    continue
                
                if counter[sequence[i+1]] < counter[sequence[i]]:
                    return []
                counter[sequence[i+1]] -= counter[sequence[i]]
                res.extend([sequence[i]] * counter[sequence[i]])
                del counter[sequence[i]]
            
            if counter[sequence[-1]] != 0:
                return []
            del counter[sequence[-1]]
        
        return res


changed = [1,3,4,2,6,8]
changed = [6,3,0,1]
changed = [1, 1, 2, 2, 2, 4, 8, 8, 16, 3, 6]

print(Solution().findOriginalArray(changed))    
        
       