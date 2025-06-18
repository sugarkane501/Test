from typing import Optional

from algorithm.basic_binary_tree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.flatten(root)
        return root

    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        root.left, root.right = root.right, root.left
        self.flatten(root.left)
        self.flatten(root.right)