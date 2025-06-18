from typing import Optional, List

from algorithm.basic_binary_tree import TreeNode


class Solution:
    def __init__(self):
        self.temp = {}
        self.result = []

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.traverse(root)
        return self.result

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return '#'

        left = self.traverse(root.left)
        right = self.traverse(root.right)
        str1 = left + "," + right + "," + root.val
        num = self.temp.get(str1,0)
        if num == 1:
            self.result.append(root)
        self.temp[str1] = num + 1
        return str1