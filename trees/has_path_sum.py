from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, 0)]

        while stack:
            node, curr_sum = stack.pop()

            if not node.left and not node.right:
                total_sum = node.val + curr_sum
                if total_sum == targetSum:
                    return True

            if node.right:
                stack.append((node.right, node.val + curr_sum))
            if node.left:
                stack.append((node.left, node.val + curr_sum))

        return False