from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        cur_path = []
        spath = [[]]
        dpath = [[]]
        def dfs(node: TreeNode, spath, dpath):
            if node is None:
                return
            print(node.val)
            if node.val == startValue:
                spath[0] = cur_path[:]
                print("spath", spath)
            elif node.val == destValue:
                dpath[0] = cur_path[:]
                print("dpath", dpath)

            cur_path.append("L")
            dfs(node.left, spath, dpath)
            cur_path[-1] = "R"
            dfs(node.right, spath, dpath)
            cur_path.pop()

        dfs(root, spath, dpath)
        spath, dpath = spath[0], dpath[0]
        if len(spath) == 0 or len(dpath) == 0:
            return "U" * len(spath) + "".join(dpath)
        else:
            ml = min(len(spath), len(dpath))
            i = 0
            for i in range(ml):
                if spath[i] != dpath[i]:
                    break
            if i == ml - 1 and spath[i] == dpath[i]:
                i += 1

            srcpath = "U" * (len(spath)-i)
            dstpath = "".join(dpath[i:]) if i < len(dpath) else ""
            return srcpath + dstpath
