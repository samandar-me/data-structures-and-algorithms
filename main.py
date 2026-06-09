from collections import deque

from trees.sum_of_left_leaves import Solution


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def dfs(root: TreeNode):
#     if not root:
#         return
#
#     stack = [root]
#
#     while stack:
#         s_len = len(stack)
#
#         node = stack.pop()
#
#         print(node.val)
#
#         if node.right:
#             stack.append(node.right)
#         if node.left:
#             stack.append(node.left)

# def dfs(root: TreeNode):
#     if not root:
#         return
#
#     print(root.val)
#
#     dfs(root.left)
#     dfs(root.right)

def diameterOfBinaryTree(root: TreeNode) -> int:
    diameter = 0

    def dfs(node: TreeNode) -> int:
        nonlocal diameter

        if not node:
            return 0

        leftDepth = dfs(node.left)
        rightDepth = dfs(node.right)

      #  print(leftDepth)
        print(rightDepth)

        d = leftDepth + rightDepth
        diameter = max(d, diameter)
        return max(leftDepth, rightDepth) + 1

    dfs(root)
    return diameter

if __name__ == '__main__':
    # root = TreeNode(4)
    #
    # root.left = TreeNode(9)
    # root.right = TreeNode(0)
    #
    # root.left.left = TreeNode(5)
    # root.left.right = TreeNode(1)

    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print(sol.sumOfLeftLeaves(root))

    # print(diameterOfBinaryTree(root))

