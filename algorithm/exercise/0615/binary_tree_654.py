from typing import List, Optional

from algorithm.basic_binary_tree import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.traverse(nums, 0, len(nums) - 1)
        return root

    def traverse(self, nums: List[int], lo: int, hi: int):
        if lo >= hi:
            return None

        maxVal = -1
        index = -1
        for i in range(lo, hi + 1):
            if nums[i] > maxVal:
                maxVal = nums[i]
                index = i

        node = TreeNode(maxVal)
        left = self.traverse(nums, lo, index - 1)
        right = self.traverse(nums, index + 1, hi)
        node.left = left
        node.right = right
        return node
