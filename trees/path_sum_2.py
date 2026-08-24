from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(node: Optional[TreeNode], path: list):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right:
                if sum(path) == targetSum:
                    result.append(path.copy())

            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()

        dfs(root, path)

        return result

    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    #     if not root: return []
    #
    #     result = []
    #     path = []
    #
    #     stack = [(root, 0)]
    #
    #     while stack:
    #         node, curr_sum = stack.pop()
    #
    #         if not node.left and not node.right:
    #             if node.val + curr_sum == targetSum:
    #                 print(len(stack))
    #
    #         if node.right:
    #             stack.append((node.right, node.val + curr_sum))
    #         if node.left:
    #             stack.append((node.left, node.val + curr_sum))
    #
    #     return result
