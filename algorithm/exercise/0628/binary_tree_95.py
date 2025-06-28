from typing import List, Optional

from algorithm.basic_binary_tree.TreeNode import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        res = self.traverse(1,n)
        return res

    def traverse(self, lo: int, hi: int):
        res = []

        if lo > hi :
            res.append(None)
            return res

        for i in range(lo, hi + 1):
            left = self.traverse(lo, i - 1)
            right = self.traverse(i + 1, hi)

            for lnode in left:
                for rnode in right:
                    root = TreeNode(i)
                    root.left = lnode
                    root.right =rnode
                    res.append(root)
        return res