from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return False

            path.append(node.val)

            if not node.left and not node.right:
                result = sum(path) == targetSum
                path.pop()
                return result

            if dfs(node.left):
                path.pop()
                return True

            if dfs(node.right):
                path.pop()
                return True

            path.pop()
            return False


        return dfs(root)

    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     if not root:
    #         return False
    #
    #     stack = [(root, 0)]
    #
    #     while stack:
    #         node, curr_sum = stack.pop()
    #
    #         if not node.left and not node.right:
    #             total_sum = node.val + curr_sum
    #             if total_sum == targetSum:
    #                 return True
    #
    #         if node.right:
    #             stack.append((node.right, node.val + curr_sum))
    #         if node.left:
    #             stack.append((node.left, node.val + curr_sum))
    #
    #     return False