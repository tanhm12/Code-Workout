from typing import List

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]):
        properties.sort(reverse=True)  # attack, defense
        count = 0
        cur = properties[0][0]
        max_defense_cur = 0
        max_defense_prev = 0
        
        for i in range(len(properties)):
            a, d =  properties[i]
            
            if a != cur:
                cur = a
                max_defense_prev = max_defense_cur
            if d > max_defense_prev:
                max_defense_cur = max(d, max_defense_cur)
            
            print(cur, a, d, max_defense_prev, max_defense_cur)
            if d < max_defense_prev:
                count += 1
        
        return count
    

properties = [[5,5],[6,3],[3,6]]
# properties = [[2,2],[3,3]]
# properties = [[1,5],[10,4],[4,3]]
# properties = [[7,3], [4,4], [3,7], [3,4], [3,3], [2,4], [2,3]]
# properties = [[1,1],[2,1],[2,2],[1,2]]

print(Solution().numberOfWeakCharacters(properties))
        
        