from typing import List, Optional

from algorithm.basic_binary_tree import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.traverse(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)

    def traverse(self, inorder: List[int], postorder: List[int], inStart: int, inEnd: int, postStart: int,
                 postEnd: int):
        if inStart > inEnd:
            return None

        rootVal = postorder[postEnd]
        root = TreeNode(rootVal)
        index = 0
        for i in inorder:
            if i == rootVal:
                break
            index += 1

        root.left = self.traverse(inorder, postorder, inStart, index - 1, postStart, postStart + index - inStart -1)
        root.right = self.traverse(inorder, postorder, index + 1, inEnd, postStart + index - inStart, postEnd - 1)

        return root
