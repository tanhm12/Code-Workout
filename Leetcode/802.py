from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = set()
        check = [False for _ in range(len(graph))]
        
        def is_safe(node: int):
            if node in safe_nodes:
                return True
            elif check[node]:
                return False
            check[node] = True
            for next_node in graph[node]:
                # print(node, next_node, is_safe(next_node))
                if not is_safe(next_node):
                    return False
            safe_nodes.add(node)
            return True
        
        for node in range(len(graph)):
            is_safe(node)
        return sorted(list(safe_nodes))

graph = [[1,2],[2,3],[5],[0],[5],[],[]]    
print(Solution().eventualSafeNodes(graph))
    