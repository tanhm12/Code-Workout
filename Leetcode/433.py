from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def is_neighbor(g1, g2):
            count = 0
            for i in range(len(g1)):
                if g1[i] != g2[i]:
                    count += 1
                    if count > 1:
                        break
            if count == 1:
                return True
            return False
        
        
        from queue import Queue
        q = Queue()
        check =  {s: False for s in bank}
        for s in bank:
            if is_neighbor(start, s):
                q.put((s, 1))
        
        while not q.empty():
            cs, cnt = q.get()
            check[cs] = True
            if cs == end:
                return cnt
            for s in bank:
                if not check[s] and is_neighbor(cs, s):
                    q.put((s, cnt+1))
        
        return -1

