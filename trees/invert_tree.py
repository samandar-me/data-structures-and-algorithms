from typing import Optional


class TreeNode:
    def __init__(self, val: int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode) -> Optional[TreeNode]:
    if not root:
        return None

    dfs(root)

    return root


def dfs(root: TreeNode):
    if not root:
        return

    val = root.left
    root.left = root.right
    root.right = val

    dfs(root.left)
    dfs(root.right)