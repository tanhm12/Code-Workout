from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        
class Solution:
    def levelOrder(root: Optional[TreeNode]):
        if root is None:
            return []
        res = [[root.val]]
        
        def travel(node: TreeNode, h):
            if node.left is not None:
                if h+1 >= len(res):
                    res.append([])
                res[h+1].append(node.left.val)
                travel(node.left, h+1)
                
            if node.right is not None:
                if h+1 >= len(res):
                    res.append([])
                res[h+1].append(node.right.val)
                travel(node.right, h+1)
            
        
        travel(root, 0)    
        
        return res 
        
        