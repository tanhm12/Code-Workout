from typing import List

class Solution:
    
    def allPathsSourceTarget(self, graph: List[List[int]]):
        res = []
        cur_sol = [0]
        cur_sol_set = set([0])
        trg = len(graph) - 1
        
        def find(src):
            if src == trg:
                res.append(cur_sol[:])
                return True
            for v in graph[src]:
                if v not in cur_sol_set:
                    cur_sol_set.add(v)
                    cur_sol.append(v)
                    find(v)
                    cur_sol_set.remove(v)
                    cur_sol.pop()
        
        find(0)
        return res
    

graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]

print(Solution().allPathsSourceTarget(graph))