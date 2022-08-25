from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode], h=0):
        if root is None:
            if h == 0:
                return True
            return True, h+1
        lbalanced, lheight = self.isBalanced(root.left, h+1)
        rbalanced, rheight = self.isBalanced(root.right, h+1)
        
        balanced = lbalanced and rbalanced and -1 <= lheight - rheight <= 1
        if h == 0:
            return balanced
        else:
            return balanced, max(lheight, rheight)


        