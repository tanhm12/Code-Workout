# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        
class Solution:
    def pathSum(root: Optional[TreeNode], targetSum: int):
        if root is None: 
            return []
        res = []
        current_sol = [0] * 5000
        current_sum = 0
        def cal_sum_child(node: TreeNode, i, current_sum, current_sol):
            current_sum += node.val
            current_sol[i] = node.val
            if node.left is not None :
                cal_sum_child(node.left, i+1, current_sum, current_sol)
            if node.right is not None:
                cal_sum_child(node.right, i+1, current_sum, current_sol)
            if node.left is None and node.right is None and current_sum == targetSum:
                res.append(current_sol[:i+1])
            
            current_sol[i] = 0
            current_sum -= node.val
            
        
        cal_sum_child(root,  0, current_sum, current_sol)
        
        return res
            
            