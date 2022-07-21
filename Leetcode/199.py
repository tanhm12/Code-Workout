from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def rightSideView(root: Optional[TreeNode]):
        if root is None:
            return []
        res = [root.val]
        
        def travel(node: TreeNode, h):
            if node.right is not None:
                if h+1 >= len(res):
                    res.append(node.right.val)
                travel(node.right, h+1)
            
            if node.left is not None:
                if h+1 >= len(res):
                    res.append(node.left.val)
                travel(node.left, h+1)
        
        travel(root, 0)    
        
        return res    
        
        