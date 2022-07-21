from typing import List

def reconstructQueue(people: List[List[int]]):
    from functools import cmp_to_key
    def compare(p1, p2):
        if p1[0] == p2[0]:
            return p2[1] - p1[1]
        return p1[0] - p2[0]

    people = sorted(people, key=cmp_to_key(compare))
    
    res = [None] * len(people)
    
    from sortedcontainers import SortedList
    all_positions = SortedList(list(range(len(people))))
    
    # for p in people:
    #     h, all_k = item
    #     all_k.sort(reverse=True)
    #     for k in all_k:
    #         pos = all_positions[k]
    #         all_positions.pop(k)
    #         res[pos] = [h, k]
            

    
    for p in people:
        res[all_positions[p[1]]] = p
        all_positions.pop(p[1])
    
    return res
    


# people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
people = [[2,4],[3,4],[9,0],[0,6],[7,1],[6,0],[7,3],[2,5],[1,1],[8,0]]
print(reconstructQueue(people))
    