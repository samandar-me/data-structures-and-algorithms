from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = 0
        path = []

        def dfs(node: Optional[TreeNode], path: list):
            nonlocal counter
            if not node: return

            path.append(node.val)



            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()

        dfs(root, path)

        return counter