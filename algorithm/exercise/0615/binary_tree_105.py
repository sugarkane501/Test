from typing import List, Optional

from algorithm.basic_binary_tree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        root = self.traverse(preorder,inorder,0,n-1)
        return root

    def traverse(self, preorder: List[int], inorder: List[int], lo: int, hi: int):
        if lo >= hi:
            return TreeNode(inorder[lo])

        rootVal = preorder[lo]
        index = self.findIndex(inorder, rootVal)
        root = TreeNode(rootVal)
        left = self.traverse(preorder, inorder, lo, index - 1)
        right = self.traverse(preorder, inorder, index + 1, hi)
        root.left = left
        root.right = right
        return root

    def findIndex(self, inorder: List[int], value: int) -> int | None:
        n = len(inorder)
        for i in range(0, n):
            if inorder[i] == value:
                return i
        return None
