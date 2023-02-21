# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def traverse(node: TreeNode):
            res = 100000
            if node.left is not None:
                minl, maxl, resl = traverse(node.left)
                res = min(resl, abs(node.val-maxl), res)
            else:
                minl = node.val
            if node.right is not None:
                minr, maxr, resr = traverse(node.right)
                res = min(resr, abs(node.val-minr), res)
            else:
                maxr = node.val
            return minl, maxr, res
        
        return traverse(root)[2]
            
        