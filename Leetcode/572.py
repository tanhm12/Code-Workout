# Definition for a binary tree node.
import hashlib
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def hash(value) ->str:
            return hashlib.md5(value.encode()).hexdigest()
        
        def get_hash(node: TreeNode) -> str:
            if node is None:
                return hash("None")
            return hash(str(node.val)  + get_hash(node.left) + get_hash(node.right))
        
        dst_value = get_hash(subRoot)
        def get_hash_and_compare(node):
            if node is None:
                return hash("None"), False
            left_hash,  found = get_hash_and_compare(node.left)
            if found:
                return "", True
            right_hash,  found = get_hash_and_compare(node.right)
            if found:
                return "", True
            hash_value = hash(str(node.val)  + left_hash + right_hash)
            if hash_value == dst_value:
                return "", True
            return hash_value, False
        
        return get_hash_and_compare(root)[1]
            