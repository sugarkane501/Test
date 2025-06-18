from typing import Optional

from algorithm.basic_binary_tree.TreeNode import TreeNode


class Solution:

    def __init__(self):
        self.all = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return 0

        self.traverse(root.right)
        root.val = self.all + root.val
        self.all = root.val
        self.traverse(root.left)

