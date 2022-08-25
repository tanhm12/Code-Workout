from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], h=0):
        if root is None:
            if h == 0:
                return 0
            return 0, 0
        lmax, lheight = self.diameterOfBinaryTree(root.left, h+1)
        rmax, rheight = self.diameterOfBinaryTree(root.right, h+1)
        
        nmax = max(lmax, rmax, lheight + rheight)
        if h == 0:
            return nmax
        else:
            return nmax, max(lheight, rheight) + 1
        