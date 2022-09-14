from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def __init__(self):
        self.counter = defaultdict(int)
        
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]):
        if root is None:
            count_odd = 0
            for c in self.counter:
                if self.counter[c] % 2 == 1:
                    count_odd += 1
                    if count_odd > 1:
                        break
            return 1 if count_odd <= 1 else 0
        else:
            self.counter[root.val] += 1
            res = 0
            if root.left:
                res += self.pseudoPalindromicPaths(root.left)
            if root.right:
                res += self.pseudoPalindromicPaths(root.right)
            elif not root.left:
                res += self.pseudoPalindromicPaths(None)
            
            self.counter[root.val] -= 1
            if self.counter[root.val] == 0:
                del self.counter[root.val]
            
            return res
        