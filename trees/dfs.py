class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node: TreeNode) -> None:
    if not node:
        return

    print(node.val)

    dfs(node.left)
    dfs(node.right)


def max_depth(node: TreeNode) -> int:
    if not node:
        return 0

    return 1 + max(max_depth(node.left), max_depth(node.right))