# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def travel(node: 'TreeNode'):
            nonlocal res
            if res is not None or node is None:
                return None
            return_val = node if (node is p or node is q) else None
            left = travel(node.left)
            right = travel(node.right)
            if (left and right) or (left and return_val) or (right and return_val):
                res = node
            
            return left or right or return_val
        travel(root)
        return res