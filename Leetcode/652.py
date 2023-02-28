# Definition for a binary tree node.

from typing import Optional, List, Dict
import hashlib
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        all_hashes = defaultdict(list)
        
        def travel(node: TreeNode) -> str:
            if node is None:
                return "0"
            left = travel(node.left)
            right = travel(node.right)
            hash_of_tree = hashlib.sha256((str(node.val) + left + right).encode()).hexdigest()
            all_hashes[hash_of_tree].append(node)
            return hash_of_tree
        
        travel(root)  
        
        res = []
        for hash_ in all_hashes:
            if len(all_hashes[hash_]) > 1:
                if len(set([node.val for node in all_hashes[hash_]])) > 1:
                    raise RuntimeError(f"Same hash but different tree: {[node.val for node in all_hashes[hash_]]}")
                else:
                    res.append(all_hashes[hash_][-1])
        
        return res
        