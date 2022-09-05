

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: Node):
        if not root:
            return
        
        res = []
        def dfs(node, level):
            if node is not None:
                if level >= len(res):
                    res.append([node.val])
                else:
                    res[level].append(node.val)
                
                level += 1
                for child in node.children:
                    dfs(child, level)
        
        dfs(root, 0)
        return res
                