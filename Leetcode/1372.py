# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    
    # left is false
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def longestZigZagDirection(node: TreeNode, direction: bool) -> int:
            nonlocal res
            if node is None:
                return 0
            left = longestZigZagDirection(node.left, True)
            right = longestZigZagDirection(node.right, False)
            
            res = max(res, left, right)
            if direction:
                return right + 1
            else:
                return left + 1
        longestZigZagDirection(root, True)
        return res