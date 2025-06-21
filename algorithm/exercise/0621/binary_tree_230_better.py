
# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # 节点的值
        self.left = left    # 左子节点
        self.right = right  # 右子节点

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 统计左子树的节点数量
        left = self.numberNodes(root.left)

        # 如果 k 小于等于左子树的节点数，说明第 k 小的元素在左子树中
        if k < left + 1:
            return self.kthSmallest(root.left, k)
        # 如果 k 大于左子树的节点数 + 1（当前节点），说明第 k 小的元素在右子树中
        elif k > left + 1:
            # k - (left + 1) 表示排除左子树和当前节点后，在右子树中的第 k' 小的元素
            return self.kthSmallest(root.right, k - (left + 1))
        # 如果 k == left + 1，说明当前节点就是第 k 小的元素
        else:
            return root.val

    def numberNodes(self, root: TreeNode) -> int:
        # 如果节点为空，返回 0
        if root is None:
            return 0
        # 递归计算左子树和右子树的节点数，并加上当前节点
        return self.numberNodes(root.left) + self.numberNodes(root.right) + 1
