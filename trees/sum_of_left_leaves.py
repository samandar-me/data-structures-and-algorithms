from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            if node.left and self.is_leaf(node.left):
                current = node.left.val
            else:
                current = 0

            left = dfs(node.left)
            right = dfs(node.right)

            return current + left + right

        return dfs(root)

    # def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #
    #     sum = 0
    #
    #     stack = [root]
    #
    #     while stack:
    #         node = stack.pop()
    #
    #         if node.right:
    #             stack.append(node.right)
    #
    #         if node.left:
    #             stack.append(node.left)
    #
    #             if self.is_leaf(node.left):
    #                 sum += node.left.val
    #
    #     return sum

    def is_leaf(self, root: TreeNode) -> bool:
        return root.left is None and root.right is None