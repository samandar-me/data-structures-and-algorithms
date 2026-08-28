from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        path = []

        def dfs(node: Optional[TreeNode], path: List[int]):
            nonlocal total_sum
            if not node: return

            path.append(node.val)

            if not node.left and not node.right:
                root_to_leaf = "".join(map(str, path))
                total_sum += int(root_to_leaf)

            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()

        dfs(root, path)

        return total_sum