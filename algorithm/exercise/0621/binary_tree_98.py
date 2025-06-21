from typing import Optional

from algorithm.basic_binary_tree.TreeNode import TreeNode


class Solution:

    def __init__(self):
        self.res = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root,None,None)

    def traverse(self,root: Optional[TreeNode], min: TreeNode, max: TreeNode) -> bool :
        if root is None:
            return True

        if min is not None and min.val >= root.val:
            return False

        if max is not None and max.val <= root.val:
            return False

        return self.traverse(root.left,min,root) and self.traverse(root.right,root,max)