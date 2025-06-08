
from typing import List

from algorithm.basic_binary_tree.TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.res = []

    def traverse(self,root: TreeNode) -> List[int]:
        self.traverse_1(root)
        return self.res

    def traverse_1(self,node: TreeNode):
        if node.left is None:
            return

        self.res.append(node.val)
        self.traverse_1(node.left)
        self.traverse_1(node.right)