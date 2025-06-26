from typing import Optional

from algorithm.basic_binary_tree.TreeNode import TreeNode


class Solution:

    def __init__(self):
        self.res = None

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.traverse(root,val)
        return self.res

    def traverse(self, root: Optional[TreeNode], val: int):
        if root is None:
            return

        if root.val > val:
            self.traverse(root.left,val)
        elif root.val <val:
            self.traverse(root.right,val)
        else:
            self.res = root
            return


