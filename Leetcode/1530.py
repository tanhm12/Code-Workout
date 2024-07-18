# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        all_paths = []
        current_path = []

        def dfs(node: TreeNode):
            if node is None:
                return
            current_path.append(node)
            if node.left is None and node.right is None:
                all_paths.append(current_path[:])
            else:
                dfs(node.left)
                dfs(node.right)
            current_path.pop()

        dfs(root)
        n = len(all_paths)

        def distance_between_nodes(path1, path2):
            m = min(len(path1), len(path2))
            i = 0
            for i in range(m):
                if path1[i] != path2[i]:
                    break
            # if i == m-1 and path1[i]==path2[i]:
            #     i += 1
            return len(path1) + len(path2) - 2 * i

        # print(all_paths)
        # res = []
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                d = distance_between_nodes(all_paths[i], all_paths[j])
                if d <= distance:
                    # res.append([all_paths[i][-1], all_paths[j][-1]])
                    res += 1

        return res



