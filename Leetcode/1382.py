from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        all_nodes = []

        def dfs(node: TreeNode):
            if node is None:
                return
            dfs(node.left)
            all_nodes.append(node)
            dfs(node.right)

        dfs(root)

        def bfs(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = all_nodes[mid]
            node.left = bfs(left, mid - 1)
            node.right = bfs(mid + 1, right)

            return node

        return bfs(0, len(all_nodes) - 1)