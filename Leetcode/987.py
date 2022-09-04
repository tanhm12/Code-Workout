from typing import Optional, List



# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        
        self.right = right
        
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]):
        from queue import Queue
        from collections import defaultdict
        
        res = []
        q = Queue()
        q.put([root, 0, 0])
        
        while not q.empty():
            node, row, col = q.get()
            res.append([col, row, node.val])
            
            if node.left:
                q.put([node.left, row+1, col-1])
            
            if node.right:
                q.put([node.right, row+1, col+1])
        
        res.sort()
        prev_col = res[0][0]
        final_res = [[res[0][2]]]
        for  i in range(1, len(res)):
            col, row, val = res[i]
            if col == prev_col:
                final_res[-1].append(val)
            else:
                prev_col = col
                final_res.append([val])
                    
        return final_res
        