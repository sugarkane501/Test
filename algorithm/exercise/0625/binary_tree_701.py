from typing import Optional

from algorithm.basic_binary_tree.TreeNode import TreeNode


class Solution:

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right,val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left,val)

        return root




























