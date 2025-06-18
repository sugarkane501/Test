from typing import Optional

from algorithm.basic_binary_tree import Node


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        root.next = None
        self.traverse(root.left, root.right)
        return root

    def traverse(self, node1: 'Optional[Node]', node2: 'Optional[Node]'):
        if node1 is Node and node2 is None:
            return

        node1.next = node2
        node2.next = None
        self.traverse(node1.left, node1.right)
        self.traverse(node1.right, node2.left)
        self.traverse(node2.left, node2.right)
