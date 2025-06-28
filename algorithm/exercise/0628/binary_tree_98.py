from typing import Optional

from algorithm.basic_binary_tree.TreeNode import TreeNode


class Solution:

    def __init__(self):
        self.res = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self._isValid(root,None,None)
        return self.res

    def _isValid(self,root: Optional[TreeNode], min: Optional[TreeNode], max: Optional[TreeNode]):
        if root is None:
            return True

        if min is not None and min.val >= root.val:
            return False
        if max is not None and max.val <= root.val:
            return False

        return self._isValid(root.left,min,root) and self._isValid(root.right,root,max)









