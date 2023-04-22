from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        from heapq import heapify, heappop
        
        n = len(hand)
        counter = Counter(hand)
        q = list(counter.keys())
        heapify(q)
        
        while n >= groupSize:
            while len(q) > 0 and q[0] not in counter:
                heappop(q)
            if len(q) == 0:
                break
            cur = q[0]
            for _ in range(groupSize):
                if cur not in counter:
                    return False
                counter[cur] -= 1
                if counter[cur] == 0:
                    del counter[cur]
                cur += 1
                
            n -= groupSize
        if n != 0:
            return False
        return True