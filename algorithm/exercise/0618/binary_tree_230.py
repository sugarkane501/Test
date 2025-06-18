from typing import Optional

from algorithm.basic_binary_tree import TreeNode


class Solution:
    def __init__(self):
        self.num = 0
        self.result = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root, k)
        return self.result

    def traverse(self, root: Optional[TreeNode], k: int):
        if root is None:
            return

        self.traverse(root.left,k)
        self.num +=1
        if self.num == k:
            self.result = root.val
        self.traverse(root.right,k)














































