from typing import Optional

from algorithm.basic_binary_tree.TreeNode import TreeNode


class Solution:

    def __init__(self):
        self.memo = []

    def numTrees(self, n: int) -> int:
        self.memo = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        res = self.traverse(1,n)
        return res

    def traverse(self, lo: int, hi: int):
        if lo> hi:
            return 1

        if self.memo[lo][hi] != 0:
            return self.memo[lo][hi]

        res = 0
        for i in range(lo,hi+1):
            left = self.traverse(lo,i-1)
            right = self.traverse(i+1,hi)
            res += left * right

        self.memo[lo][hi] = res
        return res