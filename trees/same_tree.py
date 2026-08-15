from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.same_tree(p, q)

    def same_tree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return self.same_tree(root1.left, root2.left) and self.same_tree(root1.right, root2.right)

    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q:
    #         return True
    #
    #     return self.bfs(p) == self.bfs(q)
    #
    # def bfs(self, root: Optional[TreeNode]) -> list:
    #     if not root:
    #         return []
    #
    #     result = []
    #
    #     m_queue = deque([root])
    #
    #     while m_queue:
    #         node = m_queue.popleft()
    #
    #         if node:
    #             result.append(node.val)
    #             m_queue.append(node.left)
    #             m_queue.append(node.right)
    #         else:
    #             result.append(None)
    #
    #
    #     return result





















