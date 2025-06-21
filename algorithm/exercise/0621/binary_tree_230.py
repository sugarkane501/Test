from typing import Optional

from algorithm.basic_binary_tree.TreeNode import TreeNode


class Solution:

    def __init__(self):

        self.num = 0
        self.temp = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root,k)
        return self.num

    def traverse(self,root: Optional[TreeNode], k: int):
        if root is None:
            return

        self.traverse(root.left,k)
        self.temp +=1
        if self.temp == k:
            self.num = root.val
        self.traverse(root.right,k)