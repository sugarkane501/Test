from typing import Optional

from algorithm.basic_binary_tree import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right is not None:
            root = root.right
        root.right = tmp
