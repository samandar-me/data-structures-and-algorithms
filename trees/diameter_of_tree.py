class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: TreeNode) -> int:
    diameter = 0

    def dfs(node: TreeNode) -> int:
        nonlocal diameter

        if not node:
            return 0

        leftDepth = dfs(node.left)
        rightDepth = dfs(node.right)
        d = leftDepth + rightDepth
        diameter = max(d, diameter)
        return max(leftDepth, rightDepth) + 1

    dfs(root)
    return diameter
