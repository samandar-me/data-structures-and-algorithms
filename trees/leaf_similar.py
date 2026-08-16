from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        root1_leaves = []
        root2_leaves = []

        def dfs(node: Optional[TreeNode], leaves):
            if not node:
                return

            if not node.left and not node.right:
                leaves.append(node.val)

            dfs(node.left, leaves)
            dfs(node.right, leaves)

        dfs(root1, root1_leaves)
        dfs(root2, root2_leaves)

        return root1_leaves == root2_leaves

