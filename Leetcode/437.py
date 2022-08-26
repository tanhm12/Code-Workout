from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self,):
        self.cur_num = 0
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int):
        def buildPrefixSum(node: TreeNode, pref_sum=0):
            if node is not None:
                node.val = [node.val, node.val + pref_sum]
                buildPrefixSum(node.left, node.val[1])
                buildPrefixSum(node.right, node.val[1])
        
        buildPrefixSum(root, 0)
        
        def calPathSumNode(node: TreeNode, start: TreeNode):
            if node is None:
                return 0
            val = node.val[1] - start.val[1] + start.val[0]
            add = 0
            if val == targetSum:
                add = 1
            return add + calPathSumNode(node.left, start) + calPathSumNode(node.right, start)
        
        
        def count(node: TreeNode):
            if node is  None:
                return 0
            return calPathSumNode(node, node) + calPathSumNode(node.left, node.left) + calPathSumNode(node.right, node.right)
        
        return count(root)
        
                
def make_binary_tree_from_array(node, arr, i):
    if arr[i] is not None:
        node.val = arr[i]
        left_i = 2*i+1
        if left_i < len(arr):
            node.left = TreeNode()
            make_binary_tree_from_array(node.left, arr, left_i)
        
        right_i = 2*i+2
        if right_i < len(arr):
            node.right = TreeNode()
            make_binary_tree_from_array(node.right, arr, right_i)

arr = []
arr = [1,None,2,None,3,None,4,None,5]

if len(arr) == 0:
    root = None
else:
    root = TreeNode()

make_binary_tree_from_array(root, arr, 0) 
        

def verify(node: TreeNode, ):
    if node is not None:
        print(node.val)
        verify(node.left)
        verify(node.right)
        
verify(root)
        