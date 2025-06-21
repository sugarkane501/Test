from typing import Optional, List

from algorithm.basic_binary_tree.TreeNode import TreeNode


class Solution:

    def __init__(self):
        # 记录所有子树以及出现的次数
        self.memo = {}
        # 记录重复的子树根节点
        self.res = []

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.traverse(root)
        return self.res

    def traverse(self,root: Optional[TreeNode]):
        if root is None:
            return "#"

        left = self.traverse(root.left)
        right = self.traverse(root.right)

        str1 = left + "," + right + "," + str(root.val)
        num = self.memo.get(str1, 0)
        if num == 1:
            self.res.append(root)
        self.memo[str1] = num + 1
        return str1